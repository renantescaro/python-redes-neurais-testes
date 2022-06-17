
CREATE DATABASE rede_neural;

CREATE TABLE registro(
  id int NOT NULL AUTO_INCREMENT,
  qtd_neuronios_camada_oculta int DEFAULT NULL,
  apredizagem float DEFAULT NULL,
  porcentagem_erro float DEFAULT NULL,
  data_inserido datetime DEFAULT NULL,
  data_finalizado datetime DEFAULT NULL,
  funcao_ativacao varchar(200) DEFAULT NULL,
  cpu varchar(100) DEFAULT NULL,
  vga varchar(100) DEFAULT NULL,
  cuda int DEFAULT 0,
  PRIMARY KEY (id)
);
