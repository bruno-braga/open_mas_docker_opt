initial_print.
+initial_print : true
  <- .print("I'm a killer agent").

@pfunction4[atomic]
+kill(AGENTID, PATH, MYNAME, SUGAR, METABOLISM, VISION) : true
  <- .print("I've received a message to kill agent ",AGENTID);
     .print("Killing agent ",AGENTID);
     mylib.my_delete_ag(AGENTID, PATH, MYNAME, SUGAR, METABOLISM, VISION);
     .wait(2000);
     +killed_agent(AGENTID);
     .print("This agent has being removed from the simulation: ",AGENTID).



+old_kill(V0, V1, X, B0, B1, B2) : true
  <- .print("I've received a message to kill agent ",X);
  	 .print("Killing agent ",X);
  	 mylib.my_delete_ag(V0, V1, X, B0, B1, B2);
  	 .wait(2000);
  	 /*.kill_agent(X, 0);*/
     .print("This agent has being removed from the simulation: ",X).








+previous_information(X) : true
  <- 
  .print("Previous Information Function:");
  .print("My previous information X: ", X).

+previous_information_all(X, Y, Z) : true
  <- 
  .concat("",X, " ", Y, " ", Z, OLD2)
  .print("Previous Information Function:");
  .print("My previous information X, Y, Z: ", X, Y, Z);
  .print("My previous information OLD2: ", OLD2);
  mylib.my_delete_ag(X, Y, Z);
  /* -previous_information_all(X, Y, Z); */
  .print("Sended to aaa_my_delete_ag").



/*
FUNCIONA NORMAL COM 3
+previous_information_all(X, Y, Z) : true
  <- 
  .print("Previous Information Function:");
  .print("My previous information X, Y, Z: ", X, Y, Z).
*/

/*
+previous_information(X, Y, Z) : true
  <- 
  .print("Previous Information Function:");
  .print("My previous information X: ", X);
  .print("My previous information Y: ", Y);
  .print("My previous information Z: ", Z).
*/

/* -!kill[error(ia_failed)]       <- print("Erro no kill"). */



/*
+!a : true
  <- .print("ok, I am here").

.send(bob, achieve, a);
      .wait(100);
      .print("Killing agent bob!");
      .kill_agent(bob);

+!start : true
<- .my_name(X);
	.print("Meu nome e: ", X);
	.wait(1000);
	.print("Salvando agente...");
	.save_agent("ag1.txt");
	.print("Salvo!");
	.send(bob, tell, save_and_kill);
	.print("Mensagem enviada pra bob");
	.send(bob, tell, soma(ae, dale));
	!start.


+hello[source(A)]
	<- .print("Recebi a mensagem de ",A);
	.print("Preciso descobrir como eliminar ele");
	.kill_agent(bob);
	.print("Matei o bob, criando agente com base no asl");
	.create_agent(lalala,"aehoo.asl");
	.send(lalala, tell, hello);
	.print("Agente criado").

*/