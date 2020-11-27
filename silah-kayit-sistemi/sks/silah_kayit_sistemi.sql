-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 21 Haz 2020, 22:46:57
-- Sunucu sürümü: 10.4.11-MariaDB
-- PHP Sürümü: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `silah_kayit_sistemi`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `personel`
--

CREATE TABLE `personel` (
  `personel_id` int(11) NOT NULL,
  `personel_sicilNo` varchar(9) COLLATE utf8_turkish_ci DEFAULT NULL,
  `personel_sifre` varchar(15) COLLATE utf8_turkish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `personel`
--

INSERT INTO `personel` (`personel_id`, `personel_sicilNo`, `personel_sifre`) VALUES
(1, '123456789', '12345'),
(2, '987654321', '98765');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sahis_bilgileri`
--

CREATE TABLE `sahis_bilgileri` (
  `id` int(11) NOT NULL,
  `tc_no` varchar(11) COLLATE utf8_turkish_ci NOT NULL,
  `ad` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `soyad` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `dogum_tarihi` varchar(15) COLLATE utf8_turkish_ci NOT NULL,
  `telefon` varchar(10) COLLATE utf8_turkish_ci NOT NULL,
  `e_posta` varchar(50) COLLATE utf8_turkish_ci NOT NULL,
  `meslek` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `il` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `ev_adres` varchar(50) COLLATE utf8_turkish_ci NOT NULL,
  `is_adres` varchar(50) COLLATE utf8_turkish_ci NOT NULL,
  `silah_seri_no` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `silah_turu` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `silah_tipi` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `silah_markasi` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `silah_modeli` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `silah_kalibre_mm` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `silah_agirligi_gr` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `silah_uzunlugu_mm` varchar(25) COLLATE utf8_turkish_ci NOT NULL,
  `silah_kapasitesi` varchar(25) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `sahis_bilgileri`
--

INSERT INTO `sahis_bilgileri` (`id`, `tc_no`, `ad`, `soyad`, `dogum_tarihi`, `telefon`, `e_posta`, `meslek`, `il`, `ev_adres`, `is_adres`, `silah_seri_no`, `silah_turu`, `silah_tipi`, `silah_markasi`, `silah_modeli`, `silah_kalibre_mm`, `silah_agirligi_gr`, `silah_uzunlugu_mm`, `silah_kapasitesi`) VALUES
(57, '100', 'Gürhan', 'Tekoğlu', '30Kasım2000', '5438298839', 'gurhan_tekoglu@hotmail.com', 'Emniyet Mensubu', 'Giresun', 'Gedikkaya Mh.', 'Giresun İl Emniyet Müdürlüğü', '1', 'Hafif Silahlar', 'Tabanca', 'GİRSAN', 'YAVUZ16 REGARD', '9', '874', '217', '14+1'),
(58, '200', 'Berkan', 'Çelik', '25Temmuz2000', '5421234567', 'berkan_celik@hotmail.com', 'Emniyet Mensubu', 'İstanbul', 'Sancaktepe', 'İstanbul Sancaktepe Muhtarlığı', '2', 'Hafif Silahlar', 'Tabanca', 'GLOCK', 'G19', '9', '900', '185', '19+1');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `personel`
--
ALTER TABLE `personel`
  ADD PRIMARY KEY (`personel_id`);

--
-- Tablo için indeksler `sahis_bilgileri`
--
ALTER TABLE `sahis_bilgileri`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `personel`
--
ALTER TABLE `personel`
  MODIFY `personel_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `sahis_bilgileri`
--
ALTER TABLE `sahis_bilgileri`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
