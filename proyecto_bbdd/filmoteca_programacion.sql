-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-05-2022 a las 09:57:26
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `filmoteca_programacion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `cod_persona` mediumint(8) UNSIGNED NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `fecNac` date NOT NULL,
  `nacionalidad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`cod_persona`, `nombre`, `apellidos`, `fecNac`, `nacionalidad`) VALUES
(1, 'David', 'Attenborough', '1926-05-08', 'Británica'),
(2, 'Bryan', 'Cranston', '1956-03-07', 'Estadounidense'),
(3, 'Aaron', 'Paul', '1979-08-27', 'Estadounidense'),
(4, 'Anna', 'Gunn', '1968-08-11', 'Estadounidense'),
(5, 'Bob', 'Odenkirk', '1962-10-22', 'Estadounidense'),
(6, 'Krysten', 'Ritter', '1981-12-16', 'Estadounidense'),
(7, 'Damian', 'Lewis', '1971-02-11', 'Británica'),
(8, 'Ron', 'Livingston', '1967-06-05', 'Estadounidense'),
(9, 'Michael', 'Cudlitz', '1964-12-29', 'Estadounidense'),
(10, 'Michael', 'Fassbender', '1977-04-02', 'Alemana'),
(11, 'Donnie', 'Wahlberg', '1969-08-17', 'Estadounidense'),
(12, 'Jared', 'Harris', '1961-08-24', 'Británica'),
(13, 'Stellan', 'Skarsgård', '1951-06-13', 'Sueca'),
(14, 'Emily', 'Watson', '1967-01-14', 'Británica'),
(15, 'Dominic', 'West', '1969-10-15', 'Británica'),
(16, 'John', 'Doman', '1945-01-09', 'Estadounidense'),
(17, 'Idris', 'Elba', '1972-09-06', 'Británica'),
(18, 'Frankie', 'Faison', '1949-06-10', 'Estadounidense'),
(19, 'Larry', 'Gilliard', '1971-09-22', 'Estadounidense'),
(20, 'Sam', 'Worthington', '1976-08-02', 'Australiano'),
(21, 'Zoe', 'Saldaña', '1978-06-17', 'Estadounidense'),
(22, 'Sigourney', 'Weaver', '1849-10-08', 'Estadounidense'),
(23, 'Michelle', 'Rodríguez', '1978-07-12', 'Estadounidense'),
(24, 'Stephen', 'Lang', '1952-07-11', 'Estadounidense'),
(25, 'Neil', 'Tyson', '1958-10-05', 'Estadounidense'),
(26, 'Carl', 'Sagan', '1934-11-09', 'Estadounidense'),
(27, 'Peter', 'Emshwiller', '1952-10-19', 'Estadounidense'),
(28, 'Seth', 'McFarlane', '1973-10-26', 'Estadounidense'),
(29, 'Paul', 'Telfer', '1979-10-30', 'Británica'),
(30, 'James', 'Gandolfini', '1961-09-16', 'Estadounidense'),
(31, 'Lorraine', 'Bracco', '1954-10-02', 'Estadounidense'),
(32, 'Edith', 'Falco', '1963-07-05', 'Estadounidense'),
(33, 'Michael', 'Imperioli', '1966-03-26', 'Estadounidense'),
(34, 'Dominic', 'Chianese', '1931-02-24', 'Estadounidense'),
(35, 'Vince', 'Gilligan', '1967-02-10', 'Estadounidense'),
(36, 'Alastair', 'Fothergill', '1960-04-10', 'Británica'),
(37, 'Mikael', 'Salomon', '1945-02-24', 'Danesa'),
(38, 'Johan', 'Renck', '1966-12-05', 'Sueca'),
(39, 'David', 'Simon', '1960-02-09', 'Estadounidense'),
(40, 'James', 'Cameron', '1954-08-16', 'Canadiense'),
(41, 'David', 'Chase', '1945-08-22', 'Estadounidense');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `series`
--

CREATE TABLE `series` (
  `cod_serie` mediumint(8) UNSIGNED NOT NULL,
  `titulo` varchar(150) NOT NULL,
  `numTemporadas` tinyint(3) UNSIGNED NOT NULL,
  `enlace` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `series`
--

INSERT INTO `series` (`cod_serie`, `titulo`, `numTemporadas`, `enlace`) VALUES
(1, 'Planeta Tierra II', 1, 'https://cutt.ly/nF9Jo6U'),
(2, 'Breaking Bad', 5, 'https://cutt.ly/zF9LWXE'),
(3, 'Planeta Tierra', 1, 'https://cutt.ly/HF9XQG4'),
(4, 'Hermanos de sangre', 1, 'https://cutt.ly/aF9X9bM'),
(5, 'Chernobyl', 1, 'https://cutt.ly/xF9ClDT'),
(6, 'The Wire (Bajo escucha)', 5, 'https://cutt.ly/CF9CEGD'),
(7, 'Planeta azul II', 1, 'https://cutt.ly/ZF9VscQ'),
(8, 'Avatar: La leyenda de Aang', 3, 'https://cutt.ly/bF9BqXn'),
(9, 'Cosmos: Una odisea en el espacio-tiempo', 1, 'https://cutt.ly/QF9Bfg2'),
(10, 'Los Soprano', 6, 'https://cutt.ly/UF9M488');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `seriespersonas`
--

CREATE TABLE `seriespersonas` (
  `cod_serie` mediumint(8) UNSIGNED NOT NULL,
  `cod_persona` mediumint(8) UNSIGNED NOT NULL,
  `rol` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `seriespersonas`
--

INSERT INTO `seriespersonas` (`cod_serie`, `cod_persona`, `rol`) VALUES
(1, 1, 'actor/director'),
(2, 2, 'actor'),
(2, 3, 'actor'),
(2, 4, 'actor'),
(2, 5, 'actor'),
(2, 6, 'actor'),
(2, 35, 'director'),
(3, 1, 'actor'),
(3, 36, 'director'),
(4, 7, 'actor'),
(4, 8, 'actor'),
(4, 9, 'actor'),
(4, 10, 'actor'),
(4, 11, 'actor'),
(4, 37, 'director'),
(5, 12, 'actor'),
(5, 13, 'actor'),
(5, 14, 'actor'),
(5, 38, 'director'),
(6, 15, 'actor'),
(6, 16, 'actor'),
(6, 17, 'actor'),
(6, 18, 'actor'),
(6, 19, 'actor'),
(6, 40, 'director'),
(7, 1, 'actor/director'),
(8, 1, 'director'),
(8, 20, 'actor'),
(8, 21, 'actor'),
(8, 22, 'actor'),
(8, 23, 'actor'),
(8, 24, 'actor'),
(9, 25, 'actor/director'),
(9, 26, 'actor'),
(9, 27, 'actor'),
(9, 28, 'actor'),
(9, 29, 'actor'),
(10, 30, 'actor'),
(10, 31, 'actor'),
(10, 32, 'actor'),
(10, 33, 'actor'),
(10, 34, 'actor'),
(10, 41, 'director');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`cod_persona`),
  ADD UNIQUE KEY `i_nombre_apellidos` (`nombre`,`apellidos`);

--
-- Indices de la tabla `series`
--
ALTER TABLE `series`
  ADD PRIMARY KEY (`cod_serie`),
  ADD UNIQUE KEY `titulo` (`titulo`),
  ADD UNIQUE KEY `enlace` (`enlace`);

--
-- Indices de la tabla `seriespersonas`
--
ALTER TABLE `seriespersonas`
  ADD PRIMARY KEY (`cod_serie`,`cod_persona`),
  ADD KEY `cod_persona` (`cod_persona`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `seriespersonas`
--
ALTER TABLE `seriespersonas`
  ADD CONSTRAINT `seriespersonas_ibfk_1` FOREIGN KEY (`cod_serie`) REFERENCES `series` (`cod_serie`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `seriespersonas_ibfk_2` FOREIGN KEY (`cod_persona`) REFERENCES `personas` (`cod_persona`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
