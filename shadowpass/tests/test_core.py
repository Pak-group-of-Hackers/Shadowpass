import unittest

from shadowpass.core.breach import HaveIBeenPwnedBreachChecker
from shadowpass.core.cracktime import CrackTimeEstimator
from shadowpass.core.entropy import calculate_entropy
from shadowpass.core.generator import PasswordGenerator
from shadowpass.core.hashgen import HashGenerator
from shadowpass.core.strength import PasswordStrengthAnalyzer


class ShadowPassCoreTests(unittest.TestCase):
    def test_entropy_calculation(self):
        entropy, pool = calculate_entropy("Abc123!@")
        self.assertTrue(entropy > 0)
        self.assertEqual(pool, 94)

    def test_strength_analysis(self):
        analyzer = PasswordStrengthAnalyzer()
        report = analyzer.analyze_password("StrongP@ssw0rd123")
        self.assertEqual(report["rating"], "Very Strong")

    def test_password_generator(self):
        generator = PasswordGenerator()
        password = generator.generate(length=16, uppercase=True, digits=True, symbols=True)
        self.assertEqual(len(password), 16)

    def test_hash_generator(self):
        hasher = HashGenerator()
        self.assertEqual(hasher.md5("abc"), "900150983cd24fb0d6963f7d28e17f72")
        self.assertEqual(hasher.sha1("abc"), "a9993e364706816aba3e25717850c26c9cd0d89d")
        self.assertEqual(hasher.sha256("abc"), "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_crack_time_estimator(self):
        estimator = CrackTimeEstimator()
        results = estimator.estimate("P@ssw0rd123456!")
        self.assertIn("online", results)

    def test_breach_checker(self):
        checker = HaveIBeenPwnedBreachChecker()
        self.assertIsInstance(checker.check_password("password"), tuple)


if __name__ == "__main__":
    unittest.main()
