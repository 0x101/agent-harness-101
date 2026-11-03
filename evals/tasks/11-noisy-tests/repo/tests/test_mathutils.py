import unittest
from mathutils import mean, median, clamp


class Noisy(unittest.TestCase):
    def test_mean_000(self):
        data = list(range(0, 0 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 0 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_001(self):
        data = list(range(1, 1 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 1 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_002(self):
        data = list(range(2, 2 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 2 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_003(self):
        data = list(range(3, 3 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 3 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_004(self):
        data = list(range(4, 4 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 4 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_005(self):
        data = list(range(5, 5 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 5 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_006(self):
        data = list(range(6, 6 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 6 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_007(self):
        data = list(range(7, 7 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 7 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_008(self):
        data = list(range(8, 8 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 8 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_009(self):
        data = list(range(9, 9 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 9 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_010(self):
        data = list(range(10, 10 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 10 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_011(self):
        data = list(range(11, 11 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 11 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_012(self):
        data = list(range(12, 12 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 12 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_013(self):
        data = list(range(13, 13 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 13 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_014(self):
        data = list(range(14, 14 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 14 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_015(self):
        data = list(range(15, 15 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 15 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_016(self):
        data = list(range(16, 16 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 16 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_017(self):
        data = list(range(17, 17 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 17 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_018(self):
        data = list(range(18, 18 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 18 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_019(self):
        data = list(range(19, 19 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 19 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_020(self):
        data = list(range(20, 20 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 20 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_021(self):
        data = list(range(21, 21 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 21 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_022(self):
        data = list(range(22, 22 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 22 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_023(self):
        data = list(range(23, 23 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 23 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_024(self):
        data = list(range(24, 24 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 24 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_025(self):
        data = list(range(25, 25 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 25 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_026(self):
        data = list(range(26, 26 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 26 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_027(self):
        data = list(range(27, 27 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 27 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_028(self):
        data = list(range(28, 28 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 28 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_029(self):
        data = list(range(29, 29 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 29 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_030(self):
        data = list(range(30, 30 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 30 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_031(self):
        data = list(range(31, 31 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 31 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_032(self):
        data = list(range(32, 32 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 32 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_033(self):
        data = list(range(33, 33 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 33 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_034(self):
        data = list(range(34, 34 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 34 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_035(self):
        data = list(range(35, 35 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 35 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_036(self):
        data = list(range(36, 36 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 36 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_037(self):
        data = list(range(37, 37 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 37 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_038(self):
        data = list(range(38, 38 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 38 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_039(self):
        data = list(range(39, 39 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 39 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_040(self):
        data = list(range(40, 40 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 40 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_041(self):
        data = list(range(41, 41 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 41 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_042(self):
        data = list(range(42, 42 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 42 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_043(self):
        data = list(range(43, 43 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 43 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_044(self):
        data = list(range(44, 44 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 44 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_045(self):
        data = list(range(45, 45 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 45 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_046(self):
        data = list(range(46, 46 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 46 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_047(self):
        data = list(range(47, 47 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 47 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_048(self):
        data = list(range(48, 48 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 48 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_049(self):
        data = list(range(49, 49 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 49 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_050(self):
        data = list(range(50, 50 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 50 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_051(self):
        data = list(range(51, 51 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 51 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_052(self):
        data = list(range(52, 52 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 52 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_053(self):
        data = list(range(53, 53 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 53 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_054(self):
        data = list(range(54, 54 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 54 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_055(self):
        data = list(range(55, 55 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 55 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_056(self):
        data = list(range(56, 56 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 56 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_057(self):
        data = list(range(57, 57 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 57 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_058(self):
        data = list(range(58, 58 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 58 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_059(self):
        data = list(range(59, 59 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 59 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_060(self):
        data = list(range(60, 60 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 60 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_061(self):
        data = list(range(61, 61 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 61 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_062(self):
        data = list(range(62, 62 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 62 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_063(self):
        data = list(range(63, 63 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 63 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_064(self):
        data = list(range(64, 64 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 64 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_065(self):
        data = list(range(65, 65 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 65 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_066(self):
        data = list(range(66, 66 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 66 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_067(self):
        data = list(range(67, 67 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 67 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_068(self):
        data = list(range(68, 68 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 68 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_069(self):
        data = list(range(69, 69 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 69 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_070(self):
        data = list(range(70, 70 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 70 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_071(self):
        data = list(range(71, 71 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 71 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_072(self):
        data = list(range(72, 72 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 72 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_073(self):
        data = list(range(73, 73 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 73 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_074(self):
        data = list(range(74, 74 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 74 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_075(self):
        data = list(range(75, 75 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 75 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_076(self):
        data = list(range(76, 76 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 76 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_077(self):
        data = list(range(77, 77 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 77 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_078(self):
        data = list(range(78, 78 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 78 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_079(self):
        data = list(range(79, 79 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 79 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_080(self):
        data = list(range(80, 80 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 80 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_081(self):
        data = list(range(81, 81 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 81 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_082(self):
        data = list(range(82, 82 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 82 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_083(self):
        data = list(range(83, 83 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 83 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_084(self):
        data = list(range(84, 84 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 84 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_085(self):
        data = list(range(85, 85 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 85 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_086(self):
        data = list(range(86, 86 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 86 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_087(self):
        data = list(range(87, 87 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 87 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_088(self):
        data = list(range(88, 88 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 88 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_089(self):
        data = list(range(89, 89 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 89 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_090(self):
        data = list(range(90, 90 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 90 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_091(self):
        data = list(range(91, 91 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 91 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_092(self):
        data = list(range(92, 92 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 92 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_093(self):
        data = list(range(93, 93 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 93 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_094(self):
        data = list(range(94, 94 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 94 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_095(self):
        data = list(range(95, 95 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 95 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_096(self):
        data = list(range(96, 96 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 96 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_097(self):
        data = list(range(97, 97 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 97 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_098(self):
        data = list(range(98, 98 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 98 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_099(self):
        data = list(range(99, 99 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 99 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_100(self):
        data = list(range(100, 100 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 100 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_101(self):
        data = list(range(101, 101 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 101 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_102(self):
        data = list(range(102, 102 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 102 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_103(self):
        data = list(range(103, 103 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 103 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_104(self):
        data = list(range(104, 104 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 104 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_105(self):
        data = list(range(105, 105 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 105 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_106(self):
        data = list(range(106, 106 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 106 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_107(self):
        data = list(range(107, 107 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 107 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_108(self):
        data = list(range(108, 108 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 108 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_109(self):
        data = list(range(109, 109 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 109 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_110(self):
        data = list(range(110, 110 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 110 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_111(self):
        data = list(range(111, 111 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 111 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_112(self):
        data = list(range(112, 112 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 112 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_113(self):
        data = list(range(113, 113 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 113 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_114(self):
        data = list(range(114, 114 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 114 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_115(self):
        data = list(range(115, 115 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 115 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_116(self):
        data = list(range(116, 116 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 116 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_117(self):
        data = list(range(117, 117 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 117 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_118(self):
        data = list(range(118, 118 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 118 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_119(self):
        data = list(range(119, 119 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 119 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_120(self):
        data = list(range(120, 120 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 120 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_121(self):
        data = list(range(121, 121 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 121 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_122(self):
        data = list(range(122, 122 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 122 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_123(self):
        data = list(range(123, 123 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 123 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_124(self):
        data = list(range(124, 124 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 124 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_125(self):
        data = list(range(125, 125 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 125 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_126(self):
        data = list(range(126, 126 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 126 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_127(self):
        data = list(range(127, 127 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 127 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_128(self):
        data = list(range(128, 128 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 128 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_129(self):
        data = list(range(129, 129 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 129 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_130(self):
        data = list(range(130, 130 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 130 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_131(self):
        data = list(range(131, 131 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 131 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_132(self):
        data = list(range(132, 132 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 132 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_133(self):
        data = list(range(133, 133 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 133 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_134(self):
        data = list(range(134, 134 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 134 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_135(self):
        data = list(range(135, 135 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 135 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_136(self):
        data = list(range(136, 136 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 136 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_137(self):
        data = list(range(137, 137 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 137 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_138(self):
        data = list(range(138, 138 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 138 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_139(self):
        data = list(range(139, 139 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 139 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_140(self):
        data = list(range(140, 140 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 140 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_141(self):
        data = list(range(141, 141 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 141 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_142(self):
        data = list(range(142, 142 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 142 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_143(self):
        data = list(range(143, 143 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 143 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_144(self):
        data = list(range(144, 144 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 144 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_145(self):
        data = list(range(145, 145 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 145 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_146(self):
        data = list(range(146, 146 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 146 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_147(self):
        data = list(range(147, 147 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 147 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_148(self):
        data = list(range(148, 148 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 148 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_149(self):
        data = list(range(149, 149 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 149 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_150(self):
        data = list(range(150, 150 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 150 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_151(self):
        data = list(range(151, 151 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 151 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_152(self):
        data = list(range(152, 152 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 152 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_153(self):
        data = list(range(153, 153 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 153 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_154(self):
        data = list(range(154, 154 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 154 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_155(self):
        data = list(range(155, 155 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 155 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_156(self):
        data = list(range(156, 156 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 156 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_157(self):
        data = list(range(157, 157 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 157 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_158(self):
        data = list(range(158, 158 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 158 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_159(self):
        data = list(range(159, 159 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 159 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_160(self):
        data = list(range(160, 160 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 160 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_161(self):
        data = list(range(161, 161 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 161 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_162(self):
        data = list(range(162, 162 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 162 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_163(self):
        data = list(range(163, 163 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 163 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_164(self):
        data = list(range(164, 164 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 164 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_165(self):
        data = list(range(165, 165 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 165 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_166(self):
        data = list(range(166, 166 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 166 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_167(self):
        data = list(range(167, 167 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 167 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_168(self):
        data = list(range(168, 168 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 168 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_169(self):
        data = list(range(169, 169 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 169 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_170(self):
        data = list(range(170, 170 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 170 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_171(self):
        data = list(range(171, 171 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 171 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_172(self):
        data = list(range(172, 172 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 172 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_173(self):
        data = list(range(173, 173 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 173 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_174(self):
        data = list(range(174, 174 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 174 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_175(self):
        data = list(range(175, 175 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 175 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_176(self):
        data = list(range(176, 176 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 176 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_177(self):
        data = list(range(177, 177 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 177 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_178(self):
        data = list(range(178, 178 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 178 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_179(self):
        data = list(range(179, 179 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 179 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_180(self):
        data = list(range(180, 180 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 180 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_181(self):
        data = list(range(181, 181 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 181 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_182(self):
        data = list(range(182, 182 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 182 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_183(self):
        data = list(range(183, 183 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 183 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_184(self):
        data = list(range(184, 184 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 184 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_185(self):
        data = list(range(185, 185 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 185 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_186(self):
        data = list(range(186, 186 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 186 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_187(self):
        data = list(range(187, 187 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 187 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_188(self):
        data = list(range(188, 188 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 188 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_189(self):
        data = list(range(189, 189 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 189 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_190(self):
        data = list(range(190, 190 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 190 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_191(self):
        data = list(range(191, 191 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 191 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_192(self):
        data = list(range(192, 192 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 192 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_193(self):
        data = list(range(193, 193 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 193 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_194(self):
        data = list(range(194, 194 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 194 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_195(self):
        data = list(range(195, 195 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 195 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_196(self):
        data = list(range(196, 196 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 196 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_197(self):
        data = list(range(197, 197 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 197 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_198(self):
        data = list(range(198, 198 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 198 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_199(self):
        data = list(range(199, 199 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 199 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_200(self):
        data = list(range(200, 200 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 200 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_201(self):
        data = list(range(201, 201 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 201 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_202(self):
        data = list(range(202, 202 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 202 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_203(self):
        data = list(range(203, 203 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 203 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_204(self):
        data = list(range(204, 204 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 204 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_205(self):
        data = list(range(205, 205 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 205 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_206(self):
        data = list(range(206, 206 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 206 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_207(self):
        data = list(range(207, 207 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 207 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_208(self):
        data = list(range(208, 208 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 208 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_209(self):
        data = list(range(209, 209 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 209 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_210(self):
        data = list(range(210, 210 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 210 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_211(self):
        data = list(range(211, 211 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 211 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_212(self):
        data = list(range(212, 212 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 212 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_213(self):
        data = list(range(213, 213 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 213 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_214(self):
        data = list(range(214, 214 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 214 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_215(self):
        data = list(range(215, 215 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 215 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_216(self):
        data = list(range(216, 216 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 216 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_217(self):
        data = list(range(217, 217 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 217 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_218(self):
        data = list(range(218, 218 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 218 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_219(self):
        data = list(range(219, 219 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 219 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_220(self):
        data = list(range(220, 220 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 220 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_221(self):
        data = list(range(221, 221 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 221 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_222(self):
        data = list(range(222, 222 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 222 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_223(self):
        data = list(range(223, 223 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 223 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_224(self):
        data = list(range(224, 224 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 224 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_225(self):
        data = list(range(225, 225 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 225 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_226(self):
        data = list(range(226, 226 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 226 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_227(self):
        data = list(range(227, 227 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 227 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_228(self):
        data = list(range(228, 228 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 228 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_229(self):
        data = list(range(229, 229 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 229 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_230(self):
        data = list(range(230, 230 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 230 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_231(self):
        data = list(range(231, 231 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 231 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_232(self):
        data = list(range(232, 232 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 232 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_233(self):
        data = list(range(233, 233 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 233 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_234(self):
        data = list(range(234, 234 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 234 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_235(self):
        data = list(range(235, 235 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 235 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_236(self):
        data = list(range(236, 236 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 236 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_237(self):
        data = list(range(237, 237 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 237 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_238(self):
        data = list(range(238, 238 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 238 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_239(self):
        data = list(range(239, 239 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 239 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_240(self):
        data = list(range(240, 240 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 240 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_241(self):
        data = list(range(241, 241 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 241 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_242(self):
        data = list(range(242, 242 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 242 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_243(self):
        data = list(range(243, 243 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 243 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_244(self):
        data = list(range(244, 244 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 244 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_245(self):
        data = list(range(245, 245 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 245 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_246(self):
        data = list(range(246, 246 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 246 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_247(self):
        data = list(range(247, 247 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 247 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_248(self):
        data = list(range(248, 248 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 248 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_249(self):
        data = list(range(249, 249 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 249 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_250(self):
        data = list(range(250, 250 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 250 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_251(self):
        data = list(range(251, 251 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 251 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_252(self):
        data = list(range(252, 252 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 252 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_253(self):
        data = list(range(253, 253 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 253 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_254(self):
        data = list(range(254, 254 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 254 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_255(self):
        data = list(range(255, 255 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 255 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_256(self):
        data = list(range(256, 256 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 256 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_257(self):
        data = list(range(257, 257 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 257 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_258(self):
        data = list(range(258, 258 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 258 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_259(self):
        data = list(range(259, 259 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 259 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_260(self):
        data = list(range(260, 260 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 260 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_261(self):
        data = list(range(261, 261 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 261 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_262(self):
        data = list(range(262, 262 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 262 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_263(self):
        data = list(range(263, 263 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 263 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_264(self):
        data = list(range(264, 264 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 264 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_265(self):
        data = list(range(265, 265 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 265 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_266(self):
        data = list(range(266, 266 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 266 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_267(self):
        data = list(range(267, 267 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 267 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_268(self):
        data = list(range(268, 268 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 268 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_269(self):
        data = list(range(269, 269 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 269 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_270(self):
        data = list(range(270, 270 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 270 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_271(self):
        data = list(range(271, 271 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 271 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_272(self):
        data = list(range(272, 272 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 272 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_273(self):
        data = list(range(273, 273 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 273 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_274(self):
        data = list(range(274, 274 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 274 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_275(self):
        data = list(range(275, 275 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 275 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_276(self):
        data = list(range(276, 276 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 276 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_277(self):
        data = list(range(277, 277 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 277 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_278(self):
        data = list(range(278, 278 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 278 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_279(self):
        data = list(range(279, 279 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 279 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_280(self):
        data = list(range(280, 280 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 280 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_281(self):
        data = list(range(281, 281 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 281 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_282(self):
        data = list(range(282, 282 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 282 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_283(self):
        data = list(range(283, 283 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 283 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_284(self):
        data = list(range(284, 284 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 284 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_285(self):
        data = list(range(285, 285 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 285 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_286(self):
        data = list(range(286, 286 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 286 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_287(self):
        data = list(range(287, 287 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 287 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_288(self):
        data = list(range(288, 288 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 288 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_289(self):
        data = list(range(289, 289 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 289 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_290(self):
        data = list(range(290, 290 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 290 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_291(self):
        data = list(range(291, 291 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 291 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_292(self):
        data = list(range(292, 292 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 292 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_293(self):
        data = list(range(293, 293 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 293 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_294(self):
        data = list(range(294, 294 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 294 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_295(self):
        data = list(range(295, 295 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 295 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_296(self):
        data = list(range(296, 296 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 296 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_297(self):
        data = list(range(297, 297 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 297 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_298(self):
        data = list(range(298, 298 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 298 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_mean_299(self):
        data = list(range(299, 299 + 20))
        for k, x in enumerate(data):
            print(f"[trace] mean case 299 item {k} value={x} running={sum(data[:k+1])}")
        self.assertAlmostEqual(mean(data), sum(data) / len(data))

    def test_median_odd(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_median_even(self):
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_clamp(self):
        self.assertEqual(clamp(5, 0, 3), 3)


if __name__ == "__main__":
    unittest.main()
