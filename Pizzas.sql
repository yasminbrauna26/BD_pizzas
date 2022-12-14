CREATE DATABASE Pizzas;
USE Pizzas;

CREATE TABLE pizzas (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(45),
    id_sabor INT,
    descricao TEXT,
	FOREIGN KEY (id_sabor) REFERENCES sabores (id)
    
);

CREATE TABLE sabores (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(45),
    preco INT,
    id_tamanho INT,
    FOREIGN KEY (id_tamanho) REFERENCES tamanhos (id)
);

CREATE TABLE tamanhos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL
);

select * from sabores;
select * from pizzas;
select * from tamanhos;
show tables;

SELECT p.id, p.nome as pizza, p.id_sabor, s.nome AS sabor FROM pizzas p JOIN sabores s ON p.id_sabor = s.id;
SELECT p.id, p.nome as pizza, p.id_sabor, s.nome AS sabor FROM pizzas p JOIN sabores s ON p.id_sabor = s.id;

SELECT p.id, p.nome as pizza, p.id_sabor, s.nome AS sabor, p.descricao FROM pizzas p JOIN sabores s ON p.id_sabor = s.id;
SELECT s.id, s.nome AS sabor, s.preco, s.id_tamanho, t.nome AS tamanho FROM sabores s JOIN tamanhos t ON s.id_tamanho = t.id;
show databases;
