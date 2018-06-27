CREATE TABLE `ArquivoReferencia` (
	`id` bigint(128) NOT NULL,
	`nome` varchar(255),
	`localVideo` varchar(255) NOT NULL,
	`resolucao` varchar(255),
	`duracaoSegundos` int(5),
	`quadrosSegundos` varchar(6),
	`codec` varchar(10),
	PRIMARY KEY (`id`) ); CREATE TABLE `HashReferencia` (
	`id` (128) NOT NULL AUTO_INCREMENT,
	`videoID` (128) NOT NULL,
	`NomeQuadro` varchar(255) NOT NULL UNIQUE,
	`localQuadro` varchar(255) NOT NULL,
	`tempoQuadro` varchar(10) NOT NULL,
	`aHash` varchar(16) NOT NULL,
	`dHash` varchar(16) NOT NULL,
	`pHash` varchar(16) NOT NULL,
	`wHash` varchar(16) NOT NULL,
	PRIMARY KEY (`id`) ); CREATE TABLE `ArquivoComparacao` (
	`id` bigint(128) NOT NULL,
	`nome` varchar(255),
	`localVideo` varchar(255) NOT NULL,
	`resolucao` varchar(255),
	`duracaoSegundos` int(5),
	`quadrosSegundos` varchar(6),
	`codec` varchar(10),
	PRIMARY KEY (`id`) ); CREATE TABLE `HashComparacao` (
	`id` bigint(128) NOT NULL,
	`videoID` (128) NOT NULL,
	`NomeQuadro` varchar(255) NOT NULL UNIQUE,
	`localQuadro` varchar(255) NOT NULL,
	`tempoQuadro` varchar(10) NOT NULL,
	`aHash` varchar(16) NOT NULL,
	`dHash` varchar(16) NOT NULL,
	`pHash` varchar(16) NOT NULL,
	`wHash` varchar(16) NOT NULL,
	PRIMARY KEY (`id`) ); ALTER TABLE `HashReferencia` ADD CONSTRAINT `HashReferencia_fk0` FOREIGN KEY (`videoID`) 
REFERENCES `ArquivoReferencia`(`id`); ALTER TABLE `HashComparacao` ADD CONSTRAINT `HashComparacao_fk0` FOREIGN KEY (`videoID`) 
REFERENCES `ArquivoComparacao`(`id`);
