/*
CREATE TABLE nome_tabela(
    col tipo PRIMARY KEY NOT NULL
);
*/

CREATE TABLE agenda(
    ID INT PRIMARY KEY NOT NULL,
    NOME TEXT
);

INSERT INTO agenda (ID, NOME)
VALUES
(1,"João");

INSERT INTO agenda (ID, NOME)
VALUES
(2,"Maria");

INSERT INTO agenda (ID, NOME)
VALUES
(3,"José");

SELECT * FROM agenda;