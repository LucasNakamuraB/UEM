link: https://app.brmodeloweb.com/publicview/6a8703b56aeb663e94d2d5f5

Justificativas:
1) Foi criada uma entidade funcionário que gera duas outras entidades, mecânico
e atendente, para que os funcionários possam ser associados mesmo tendo 
relacionamentos e atributos diferentes 

2) Ele está em um relacionamento direto com OS para que sejam acessados
isoladamente as ordens e em um ternário com OS e Funcinário, para que se 
relacione com o funcionário e um serviço específico

3) Como só é necessário relacionar Serviço e Funcionário dentro de uma OS,
existe uma relação ternária entre eles, mas existe uma relação entre OS e
Funcionário sem serviço, e 