from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["perumahan"]
collection = db["rumah"]

data_rumah = [
    {
        'kode_rumah': 'R001',
        'nama_rumah': 'Griya Sejahtera A1',
        'alamat': 'Jl. Melati No. 12, Bandung',
        'harga': 850000000,
        'luas_tanah': 120,
        'luas_bangunan': 90,
        'kamar_tidur': 3,
        'kamar_mandi': 2,
        'developer': 'PT Maju Jaya',
        'filename': 'rumah_a1.jpg'
    },
    {
        'kode_rumah': 'R002',
        'nama_rumah': 'Permata Indah B2',
        'alamat': 'Jl. Kenanga No. 5, Cimahi',
        'harga': 675000000,
        'luas_tanah': 100,
        'luas_bangunan': 70,
        'kamar_tidur': 2,
        'kamar_mandi': 1,
        'developer': 'CV Sentosa Abadi',
        'filename': 'rumah_b2.png'
    },
    {
        'kode_rumah': 'R003',
        'nama_rumah': 'Prima Residence C3',
        'alamat': 'Komplek Prima Blok C3, Sumedang',
        'harga': 1250000000,
        'luas_tanah': 160,
        'luas_bangunan': 120,
        'kamar_tidur': 4,
        'kamar_mandi': 3,
        'developer': 'PT Karya Mandiri',
        'filename': None
    },
    {
        'kode_rumah': 'R004',
        'nama_rumah': 'Villa Harmoni D4',
        'alamat': 'Jl. Raya Lembang No. 45, Bandung Barat',
        'harga': 950000000,
        'luas_tanah': 150,
        'luas_bangunan': 100,
        'kamar_tidur': 3,
        'kamar_mandi': 2,
        'developer': 'PT Maju Jaya',
        'filename': 'villa_harmoni.jpg'
    },
    {
        'kode_rumah': 'R005',
        'nama_rumah': 'Rumah Minimalis Type 36',
        'alamat': 'Perumahan Hijau Asri Blok A No. 8, Bandung',
        'harga': 450000000,
        'luas_tanah': 60,
        'luas_bangunan': 36,
        'kamar_tidur': 2,
        'kamar_mandi': 1,
        'developer': 'CV Sentosa Abadi',
        'filename': 'type36.jpg'
    },
    {
        'kode_rumah': 'R006',
        'nama_rumah': 'Mansion Elite E5',
        'alamat': 'Jl. Setiabudi No. 120, Bandung',
        'harga': 2500000000,
        'luas_tanah': 300,
        'luas_bangunan': 200,
        'kamar_tidur': 5,
        'kamar_mandi': 4,
        'developer': 'PT Karya Mandiri',
        'filename': 'mansion_elite.jpg'
    },
    {
        'kode_rumah': 'R007',
        'nama_rumah': 'Cluster Green Valley F6',
        'alamat': 'Komplek Green Valley Blok F6, Cimahi',
        'harga': 780000000,
        'luas_tanah': 110,
        'luas_bangunan': 85,
        'kamar_tidur': 3,
        'kamar_mandi': 2,
        'developer': 'PT Maju Jaya',
        'filename': 'green_valley.jpg'
    },
    {
        'kode_rumah': 'R008',
        'nama_rumah': 'Rumah Tipe 45 Modern',
        'alamat': 'Perumahan Taman Melati Blok B No. 15',
        'harga': 520000000,
        'luas_tanah': 72,
        'luas_bangunan': 45,
        'kamar_tidur': 2,
        'kamar_mandi': 1,
        'developer': 'CV Sentosa Abadi',
        'filename': 'tipe45.jpg'
    },
    {
        'kode_rumah': 'R009',
        'nama_rumah': 'Luxury Home G7',
        'alamat': 'Jl. Dago No. 88, Bandung',
        'harga': 1800000000,
        'luas_tanah': 200,
        'luas_bangunan': 150,
        'kamar_tidur': 4,
        'kamar_mandi': 3,
        'developer': 'PT Karya Mandiri',
        'filename': 'luxury_home.jpg'
    },
    {
        'kode_rumah': 'R010',
        'nama_rumah': 'Rumah Subsidi Type 21',
        'alamat': 'Perumahan Bumi Sejahtera Blok C No. 22',
        'harga': 180000000,
        'luas_tanah': 60,
        'luas_bangunan': 21,
        'kamar_tidur': 1,
        'kamar_mandi': 1,
        'developer': 'PT Maju Jaya',
        'filename': 'subsidi_type21.jpg'
    },
    {
        'kode_rumah': 'R011',
        'nama_rumah': 'Town House H8',
        'alamat': 'Jl. Soekarno Hatta No. 200, Bandung',
        'harga': 680000000,
        'luas_tanah': 90,
        'luas_bangunan': 70,
        'kamar_tidur': 2,
        'kamar_mandi': 2,
        'developer': 'CV Sentosa Abadi',
        'filename': 'townhouse.jpg'
    },
    {
        'kode_rumah': 'R012',
        'nama_rumah': 'Villa Puncak I9',
        'alamat': 'Jl. Tangkuban Perahu No. 50, Lembang',
        'harga': 1500000000,
        'luas_tanah': 250,
        'luas_bangunan': 180,
        'kamar_tidur': 5,
        'kamar_mandi': 4,
        'developer': 'PT Karya Mandiri',
        'filename': 'villa_puncak.jpg'
    },
    {
        'kode_rumah': 'R013',
        'nama_rumah': 'Rumah Type 54',
        'alamat': 'Perumahan Citra Garden Blok D No. 10',
        'harga': 620000000,
        'luas_tanah': 84,
        'luas_bangunan': 54,
        'kamar_tidur': 3,
        'kamar_mandi': 2,
        'developer': 'PT Maju Jaya',
        'filename': 'type54.jpg'
    },
    {
        'kode_rumah': 'R014',
        'nama_rumah': 'Cluster Exclusive J10',
        'alamat': 'Komplek Exclusive Residence Blok J10',
        'harga': 1100000000,
        'luas_tanah': 140,
        'luas_bangunan': 110,
        'kamar_tidur': 4,
        'kamar_mandi': 3,
        'developer': 'CV Sentosa Abadi',
        'filename': 'exclusive.jpg'
    },
    {
        'kode_rumah': 'R015',
        'nama_rumah': 'Rumah Tipe 60',
        'alamat': 'Perumahan Taman Sari Blok E No. 5',
        'harga': 750000000,
        'luas_tanah': 96,
        'luas_bangunan': 60,
        'kamar_tidur': 3,
        'kamar_mandi': 2,
        'developer': 'PT Karya Mandiri',
        'filename': 'tipe60.jpg'
    },
    {
        'kode_rumah': 'R016',
        'nama_rumah': 'Modern House K11',
        'alamat': 'Jl. Gatot Subroto No. 150, Bandung',
        'harga': 920000000,
        'luas_tanah': 130,
        'luas_bangunan': 95,
        'kamar_tidur': 3,
        'kamar_mandi': 2,
        'developer': 'PT Maju Jaya',
        'filename': 'modern_house.jpg'
    },
    {
        'kode_rumah': 'R017',
        'nama_rumah': 'Rumah Tipe 70',
        'alamat': 'Perumahan Bumi Indah Blok F No. 12',
        'harga': 880000000,
        'luas_tanah': 108,
        'luas_bangunan': 70,
        'kamar_tidur': 3,
        'kamar_mandi': 2,
        'developer': 'CV Sentosa Abadi',
        'filename': 'tipe70.jpg'
    },
    {
        'kode_rumah': 'R018',
        'nama_rumah': 'Luxury Villa L12',
        'alamat': 'Jl. Cipaganti No. 75, Bandung',
        'harga': 2200000000,
        'luas_tanah': 280,
        'luas_bangunan': 220,
        'kamar_tidur': 5,
        'kamar_mandi': 4,
        'developer': 'PT Karya Mandiri',
        'filename': 'luxury_villa.jpg'
    },
    {
        'kode_rumah': 'R019',
        'nama_rumah': 'Cluster Family M13',
        'alamat': 'Komplek Family Residence Blok M13',
        'harga': 980000000,
        'luas_tanah': 145,
        'luas_bangunan': 105,
        'kamar_tidur': 4,
        'kamar_mandi': 3,
        'developer': 'PT Maju Jaya',
        'filename': 'family_residence.jpg'
    },
    {
        'kode_rumah': 'R020',
        'nama_rumah': 'Rumah Tipe 90',
        'alamat': 'Perumahan Taman Kencana Blok G No. 8',
        'harga': 1150000000,
        'luas_tanah': 126,
        'luas_bangunan': 90,
        'kamar_tidur': 4,
        'kamar_mandi': 3,
        'developer': 'CV Sentosa Abadi',
        'filename': 'tipe90.jpg'
    },
    {
        'kode_rumah': 'R021',
        'nama_rumah': 'Executive Home N14',
        'alamat': 'Jl. Asia Afrika No. 100, Bandung',
        'harga': 1350000000,
        'luas_tanah': 170,
        'luas_bangunan': 125,
        'kamar_tidur': 4,
        'kamar_mandi': 3,
        'developer': 'PT Karya Mandiri',
        'filename': 'executive_home.jpg'
    },
    {
        'kode_rumah': 'R022',
        'nama_rumah': 'Rumah Tipe 30',
        'alamat': 'Perumahan Bumi Mas Blok H No. 20',
        'harga': 320000000,
        'luas_tanah': 60,
        'luas_bangunan': 30,
        'kamar_tidur': 1,
        'kamar_mandi': 1,
        'developer': 'PT Maju Jaya',
        'filename': 'tipe30.jpg'
    },
    {
        'kode_rumah': 'R023',
        'nama_rumah': 'Cluster Premium O15',
        'alamat': 'Komplek Premium Estate Blok O15',
        'harga': 1280000000,
        'luas_tanah': 155,
        'luas_bangunan': 115,
        'kamar_tidur': 4,
        'kamar_mandi': 3,
        'developer': 'CV Sentosa Abadi',
        'filename': 'premium_estate.jpg'
    },
    {
        'kode_rumah': 'R024',
        'nama_rumah': 'Villa Resort P16',
        'alamat': 'Jl. Maribaya No. 200, Lembang',
        'harga': 1650000000,
        'luas_tanah': 230,
        'luas_bangunan': 170,
        'kamar_tidur': 5,
        'kamar_mandi': 4,
        'developer': 'PT Karya Mandiri',
        'filename': 'villa_resort.jpg'
    },
    {
        'kode_rumah': 'R025',
        'nama_rumah': 'Rumah Tipe 75',
        'alamat': 'Perumahan Taman Indah Blok I No. 15',
        'harga': 950000000,
        'luas_tanah': 112,
        'luas_bangunan': 75,
        'kamar_tidur': 3,
        'kamar_mandi': 2,
        'developer': 'PT Maju Jaya',
        'filename': 'tipe75.jpg'
    }
]

try:
    result = collection.insert_many(data_rumah)
    print(f'Berhasil insert {len(result.inserted_ids)} data rumah!')
except Exception as e:
    print(f'Error: {e}')

