
CREATE DATABASE rede_neural;

CREATE TABLE parametro (
  id int NOT NULL AUTO_INCREMENT,
  qtd_neuronios_camada_oculta int DEFAULT NULL,
  apredizagem float DEFAULT NULL,
  porcentagem_erro float DEFAULT NULL,
  data_inserido timestamp NULL DEFAULT CURRENT_TIMESTAMP,

  PRIMARY KEY (id)
)
