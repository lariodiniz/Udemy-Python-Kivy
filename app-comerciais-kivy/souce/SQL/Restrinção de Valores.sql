/*
CREATE table nome_tabela(
    col tipo Restrições
);


--Restrições
-- DOT NULL (não deixa ser null)
-- DEFAULT (Insere como padrão caso nenhum valor seja atribuido)
-- UNIQUE (DEtermina que o valor de todos os registros sejam diferentes)
*/
CREATE TABLE agenda(
    nome TEXT UNIQUE NOT NULL,
    idade INT DEFAULT 1

);


INSERT INTO agenda (nome, idade)
VALUES
('João', 25);

INSERT INTO agenda (nome, idade)
VALUES
('Maria', 18);

INSERT INTO agenda (nome, idade)
VALUES
('José', 21);

INSERT INTO agenda (nome)
VALUES
('Pedro');

SELECT * FROM agenda;
