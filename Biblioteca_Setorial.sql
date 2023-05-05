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
  `id_area` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_area`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`livro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`livro` (
  `id_livro` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `setor` VARCHAR(45) NOT NULL,
  `autor` VARCHAR(45) NOT NULL,
  `quantidade_pag` INT NOT NULL,
  `setor_id_setor` INT NOT NULL,
  PRIMARY KEY (`id_livro`, `setor_id_setor`),
  INDEX `fk_obra_setor1_idx` (`setor_id_setor` ASC) ,
  CONSTRAINT `fk_obra_setor1`
    FOREIGN KEY (`setor_id_setor`)
    REFERENCES `mydb`.`area` (`id_area`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`exemplar`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`exemplar` (
  `id_exemplar` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `quantidade` VARCHAR(45) NOT NULL,
  `obra_id_obra` INT NOT NULL,
  `obra_setor_id_setor` INT NOT NULL,
  PRIMARY KEY (`id_exemplar`),
  INDEX `fk_exemplar_obra1_idx` (`obra_id_obra` ASC, `obra_setor_id_setor` ASC) ,
  CONSTRAINT `fk_exemplar_obra1`
    FOREIGN KEY (`obra_id_obra` , `obra_setor_id_setor`)
    REFERENCES `mydb`.`livro` (`id_livro` , `setor_id_setor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuario` (
  `matricula` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `curso` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `vinculo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`matricula`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`emprestimo` (
  `exemplar_id_exemplar` INT NOT NULL,
  `usuario_matricula` INT NOT NULL,
  `emprestimo_id` VARCHAR(45) NOT NULL,
  `data_emprestimo` VARCHAR(45) NOT NULL,
  `data_devolucao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`exemplar_id_exemplar`, `usuario_matricula`, `emprestimo_id`),
  INDEX `fk_exemplar_has_usuario_usuario1_idx` (`usuario_matricula` ASC) ,
  INDEX `fk_exemplar_has_usuario_exemplar1_idx` (`exemplar_id_exemplar` ASC) ,
  CONSTRAINT `fk_exemplar_has_usuario_exemplar1`
    FOREIGN KEY (`exemplar_id_exemplar`)
    REFERENCES `mydb`.`exemplar` (`id_exemplar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_exemplar_has_usuario_usuario1`
    FOREIGN KEY (`usuario_matricula`)
    REFERENCES `mydb`.`usuario` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
