INSERT INTO AREA(nome) VALUES('INFORMÁTICA');
INSERT INTO AREA(nome) VALUES('AGROPECUÁRIA');
INSERT INTO AREA(nome) VALUES('QUÍMICA');
SELECT * FROM AREA;
SELECT * FROM LIVRO;
SELECT * FROM USUARIO;
SELECT * FROM emprestimo;

SELECT usuario_matricula, livro_id_livro FROM emprestimo WHERE estado LIKE 'emprestado';
SELECT * FROM Livro WHERE nome LIKE 'Informática. Conceitos Básicos';
SELECT * FROM livro WHERE nome = 'Informática. Conceitos Básicos';
SELECT * FROM emprestimo WHERE usuario_matricula = 20201084010010;
UPDATE emprestimo SET estado = 'pendente' WHERE livro_id_livro = 5;