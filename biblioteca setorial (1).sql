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
-- Table `mydb`.`setor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`setor` (
  `id_setor` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_setor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`obra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`obra` (
  `id_obra` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `setor` VARCHAR(45) NOT NULL,
  `autor` VARCHAR(45) NOT NULL,
  `quantidade_pag` INT NOT NULL,
  `setor_id_setor` INT NOT NULL,
  PRIMARY KEY (`id_obra`, `setor_id_setor`),
  INDEX `fk_obra_setor1_idx` (`setor_id_setor` ASC) ,
  CONSTRAINT `fk_obra_setor1`
    FOREIGN KEY (`setor_id_setor`)
    REFERENCES `mydb`.`setor` (`id_setor`)
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
    REFERENCES `mydb`.`obra` (`id_obra` , `setor_id_setor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`aluno` (
  `matricula` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`matricula`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`professor` (
  `matricula` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `curso` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `setor_id_setor` INT NOT NULL,
  PRIMARY KEY (`matricula`),
  INDEX `fk_professor_setor1_idx` (`setor_id_setor` ASC) ,
  CONSTRAINT `fk_professor_setor1`
    FOREIGN KEY (`setor_id_setor`)
    REFERENCES `mydb`.`setor` (`id_setor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`emprestimo` (
  `id_emprestimo` INT NOT NULL,
  `data_emprestimo` DATE NOT NULL,
  `data_devolucao` DATE NOT NULL,
  `aluno_matricula` INT NOT NULL,
  `professor_matricula` INT NOT NULL,
  PRIMARY KEY (`id_emprestimo`),
  INDEX `fk_emprestimo_aluno1_idx` (`aluno_matricula` ASC) ,
  INDEX `fk_emprestimo_professor1_idx` (`professor_matricula` ASC) ,
  CONSTRAINT `fk_emprestimo_aluno1`
    FOREIGN KEY (`aluno_matricula`)
    REFERENCES `mydb`.`aluno` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_emprestimo_professor1`
    FOREIGN KEY (`professor_matricula`)
    REFERENCES `mydb`.`professor` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`exemplar_has_emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`exemplar_has_emprestimo` (
  `exemplar_id_exemplar` INT NOT NULL,
  `emprestimo_id_emprestimo` INT NOT NULL,
  PRIMARY KEY (`exemplar_id_exemplar`, `emprestimo_id_emprestimo`),
  INDEX `fk_exemplar_has_emprestimo_emprestimo1_idx` (`emprestimo_id_emprestimo` ASC) ,
  INDEX `fk_exemplar_has_emprestimo_exemplar1_idx` (`exemplar_id_exemplar` ASC) ,
  CONSTRAINT `fk_exemplar_has_emprestimo_exemplar1`
    FOREIGN KEY (`exemplar_id_exemplar`)
    REFERENCES `mydb`.`exemplar` (`id_exemplar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_exemplar_has_emprestimo_emprestimo1`
    FOREIGN KEY (`emprestimo_id_emprestimo`)
    REFERENCES `mydb`.`emprestimo` (`id_emprestimo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
