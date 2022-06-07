
CREATE DATABASE rede_neural;

CREATE TABLE registro(
  id int NOT NULL AUTO_INCREMENT,
  qtd_neuronios_camada_oculta int DEFAULT NULL,
  apredizagem float DEFAULT NULL,
  porcentagem_erro float DEFAULT NULL,
  data_inserido datetime DEFAULT NULL,
  data_finalizado datetime DEFAULT NULL,
  PRIMARY KEY (id)
);
