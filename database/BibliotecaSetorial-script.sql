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
  `link_capa` VARCHAR(200) NOT NULL,
  `descricao` VARCHAR(2000) NOT NULL,
  PRIMARY KEY (`id_livro`, `area_id_area`),
  INDEX `fk_obra_setor1_idx` (`area_id_area` ASC) ,
  CONSTRAINT `fk_obra_setor1`
    FOREIGN KEY (`area_id_area`)
    REFERENCES `mydb`.`area` (`id_area`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`avaliacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`avaliacao` (
  `id_avaliacao` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `data` DATE NOT NULL,
  `avaliacao` VARCHAR(500) NOT NULL,
  `livro_id_livro` INT(11) NOT NULL,
  `livro_area_id_area` INT(11) NOT NULL,
  PRIMARY KEY (`id_avaliacao`, `livro_id_livro`, `livro_area_id_area`),
  INDEX `fk_avaliacao_livro1_idx` (`livro_id_livro` ASC, `livro_area_id_area` ASC) ,
  CONSTRAINT `fk_avaliacao_livro1`
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
  `matricula` INT(20) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `curso` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `vinculo` VARCHAR(45) NOT NULL,
  `link_foto` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`matricula`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`emprestimo` (
  `id_emprestimo` INT(11) NOT NULL AUTO_INCREMENT,
  `livro_id_livro` INT(11) NOT NULL,
  `livro_area_id_area` INT(11) NOT NULL,
  `usuario_matricula` INT(11) NOT NULL,
  `data_emprestimo` DATE NOT NULL,
  `data_devolucao` DATE NOT NULL,
  `estado` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id_emprestimo`, `livro_id_livro`, `livro_area_id_area`, `usuario_matricula`),
  INDEX `fk_livro_has_usuario_usuario1_idx` (`usuario_matricula` ASC) ,
  INDEX `fk_livro_has_usuario_livro1_idx` (`livro_id_livro` ASC, `livro_area_id_area` ASC) ,
  CONSTRAINT `fk_livro_has_usuario_livro1`
    FOREIGN KEY (`livro_id_livro` , `livro_area_id_area`)
    REFERENCES `mydb`.`livro` (`id_livro` , `area_id_area`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_livro_has_usuario_usuario1`
    FOREIGN KEY (`usuario_matricula`)
    REFERENCES `mydb`.`usuario` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `mydb`.`pdf`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pdf` (
  `id_pdf` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `area` VARCHAR(45) NOT NULL,
  `autor` VARCHAR(45) NOT NULL,
  `quantidade_pag` INT(11) NOT NULL,
  `pdfcol` LONGBLOB NOT NULL,
  `area_id_area` INT(11) NOT NULL,
  PRIMARY KEY (`id_pdf`, `area_id_area`),
  INDEX `fk_pdf_area1_idx` (`area_id_area` ASC) ,
  CONSTRAINT `fk_pdf_area1`
    FOREIGN KEY (`area_id_area`)
    REFERENCES `mydb`.`area` (`id_area`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
