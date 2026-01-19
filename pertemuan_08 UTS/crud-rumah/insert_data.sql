-- Script SQL untuk insert data rumah contoh
-- Pastikan database dan tabel sudah dibuat terlebih dahulu
-- Gunakan: USE uts_rumah_db; sebelum menjalankan INSERT ini

USE uts_rumah_db;

-- Insert data rumah
INSERT INTO rumah (kode_rumah, nama_rumah, alamat, harga, luas_tanah, luas_bangunan, kamar_tidur, kamar_mandi, developer, filename) VALUES
('R001', 'Griya Sejahtera A1', 'Jl. Melati No. 12, Bandung', 850000000, 120, 90, 3, 2, 'PT Maju Jaya', 'rumah_a1.jpg'),
('R002', 'Permata Indah B2', 'Jl. Kenanga No. 5, Cimahi', 675000000, 100, 70, 2, 1, 'CV Sentosa Abadi', 'rumah_b2.png'),
('R003', 'Prima Residence C3', 'Komplek Prima Blok C3, Sumedang', 1250000000, 160, 120, 4, 3, 'PT Karya Mandiri', NULL),
('R004', 'Villa Harmoni D4', 'Jl. Raya Lembang No. 45, Bandung Barat', 950000000, 150, 100, 3, 2, 'PT Maju Jaya', 'villa_harmoni.jpg'),
('R005', 'Rumah Minimalis Type 36', 'Perumahan Hijau Asri Blok A No. 8, Bandung', 450000000, 60, 36, 2, 1, 'CV Sentosa Abadi', 'type36.jpg'),
('R006', 'Mansion Elite E5', 'Jl. Setiabudi No. 120, Bandung', 2500000000, 300, 200, 5, 4, 'PT Karya Mandiri', 'mansion_elite.jpg'),
('R007', 'Cluster Green Valley F6', 'Komplek Green Valley Blok F6, Cimahi', 780000000, 110, 85, 3, 2, 'PT Maju Jaya', 'green_valley.jpg'),
('R008', 'Rumah Tipe 45 Modern', 'Perumahan Taman Melati Blok B No. 15', 520000000, 72, 45, 2, 1, 'CV Sentosa Abadi', 'tipe45.jpg'),
('R009', 'Luxury Home G7', 'Jl. Dago No. 88, Bandung', 1800000000, 200, 150, 4, 3, 'PT Karya Mandiri', 'luxury_home.jpg'),
('R010', 'Rumah Subsidi Type 21', 'Perumahan Bumi Sejahtera Blok C No. 22', 180000000, 60, 21, 1, 1, 'PT Maju Jaya', 'subsidi_type21.jpg'),
('R011', 'Town House H8', 'Jl. Soekarno Hatta No. 200, Bandung', 680000000, 90, 70, 2, 2, 'CV Sentosa Abadi', 'townhouse.jpg'),
('R012', 'Villa Puncak I9', 'Jl. Tangkuban Perahu No. 50, Lembang', 1500000000, 250, 180, 5, 4, 'PT Karya Mandiri', 'villa_puncak.jpg'),
('R013', 'Rumah Type 54', 'Perumahan Citra Garden Blok D No. 10', 620000000, 84, 54, 3, 2, 'PT Maju Jaya', 'type54.jpg'),
('R014', 'Cluster Exclusive J10', 'Komplek Exclusive Residence Blok J10', 1100000000, 140, 110, 4, 3, 'CV Sentosa Abadi', 'exclusive.jpg'),
('R015', 'Rumah Tipe 60', 'Perumahan Taman Sari Blok E No. 5', 750000000, 96, 60, 3, 2, 'PT Karya Mandiri', 'tipe60.jpg'),
('R016', 'Modern House K11', 'Jl. Gatot Subroto No. 150, Bandung', 920000000, 130, 95, 3, 2, 'PT Maju Jaya', 'modern_house.jpg'),
('R017', 'Rumah Tipe 70', 'Perumahan Bumi Indah Blok F No. 12', 880000000, 108, 70, 3, 2, 'CV Sentosa Abadi', 'tipe70.jpg'),
('R018', 'Luxury Villa L12', 'Jl. Cipaganti No. 75, Bandung', 2200000000, 280, 220, 5, 4, 'PT Karya Mandiri', 'luxury_villa.jpg'),
('R019', 'Cluster Family M13', 'Komplek Family Residence Blok M13', 980000000, 145, 105, 4, 3, 'PT Maju Jaya', 'family_residence.jpg'),
('R020', 'Rumah Tipe 90', 'Perumahan Taman Kencana Blok G No. 8', 1150000000, 126, 90, 4, 3, 'CV Sentosa Abadi', 'tipe90.jpg'),
('R021', 'Executive Home N14', 'Jl. Asia Afrika No. 100, Bandung', 1350000000, 170, 125, 4, 3, 'PT Karya Mandiri', 'executive_home.jpg'),
('R022', 'Rumah Tipe 30', 'Perumahan Bumi Mas Blok H No. 20', 320000000, 60, 30, 1, 1, 'PT Maju Jaya', 'tipe30.jpg'),
('R023', 'Cluster Premium O15', 'Komplek Premium Estate Blok O15', 1280000000, 155, 115, 4, 3, 'CV Sentosa Abadi', 'premium_estate.jpg'),
('R024', 'Villa Resort P16', 'Jl. Maribaya No. 200, Lembang', 1650000000, 230, 170, 5, 4, 'PT Karya Mandiri', 'villa_resort.jpg'),
('R025', 'Rumah Tipe 75', 'Perumahan Taman Indah Blok I No. 15', 950000000, 112, 75, 3, 2, 'PT Maju Jaya', 'tipe75.jpg');

