-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`area`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`area` (
  `id_area` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_area`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`livro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`livro` (
  `id_livro` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `autor` VARCHAR(45) NOT NULL,
  `quantidade_pag` INT(11) NOT NULL,
  `area_id_area` INT(11) NOT NULL,
  `link_capa` VARCHAR(350) NOT NULL,
  PRIMARY KEY (`id_livro`, `area_id_area`),
  INDEX `fk_obra_setor1_idx` (`area_id_area` ASC) ,
  CONSTRAINT `fk_obra_setor1`
    FOREIGN KEY (`area_id_area`)
    REFERENCES `mydb`.`area` (`id_area`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`exemplar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`exemplar` (
  `id_exemplar` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `quantidade` VARCHAR(45) NOT NULL,
  `livro_id_livro` INT(11) NOT NULL,
  `livro_area_id_area` INT(11) NOT NULL,
  PRIMARY KEY (`id_exemplar`),
  INDEX `fk_exemplar_obra1_idx` (`livro_id_livro` ASC, `livro_area_id_area` ASC) ,
  CONSTRAINT `fk_exemplar_obra1`
    FOREIGN KEY (`livro_id_livro` , `livro_area_id_area`)
    REFERENCES `mydb`.`livro` (`id_livro` , `area_id_area`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuario` (
  `matricula` INT(11) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `curso` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `vinculo` VARCHAR(45) NOT NULL,
  `link_foto` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`matricula`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
