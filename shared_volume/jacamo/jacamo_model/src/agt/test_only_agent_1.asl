initial.
+initial : true
<- 
	.print("Ag1");
	
	/* Algo que é carregado entre as simulações */	
	.random(R);
	+my_testing(R);
	?my_testing(R);
	.print("R: ", R).

@pfunction4[atomic]
+kill(MSG) : true
  <- .print("Msg received: ",MSG)
     .wait(2000);
     .my_name(MYNAME);
	.concat("src/agt/list/",MYNAME,".asl",NAME)
	/* É possível salvar o agente já adicionando crenças, como o exemplo do say(hello) */	
	.save_agent(NAME,[start,say(hello)]);
	.print("Saved my information on file. Sending message to remove agent from simulation").