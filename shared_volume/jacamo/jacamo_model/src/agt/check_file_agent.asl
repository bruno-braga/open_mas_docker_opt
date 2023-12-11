!main.
@pfunction3[atomic]
+!main : true
<-
	/* .print("Hello there. I'm a checker agent"); */
	/* .print("Checking and creating agent if it exists on file"); */
	/* Calling Java code to check if there is any agent to be inserted in the simulation, from the Router (via API) */
	mylib.my_create_ag;
	.wait(1000);
	!main.