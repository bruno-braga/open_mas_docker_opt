package mylib;

import jacamo.project.JaCaMoProject;
import java.util.concurrent.TimeUnit;
import jacamo.project.JaCaMoAgentParameters;
import jacamo.infra.JaCaMoRuntimeServices;

import java.util.logging.Level;

import jaca.CAgentArch;
import jacamo.project.JaCaMoAgentParameters;
import jacamo.project.JaCaMoWorkspaceParameters;
import jason.architecture.AgArch;
import jason.asSemantics.Intention;
import jason.asSyntax.ASSyntax;
import jason.asSyntax.Atom;
import jason.asSyntax.ListTerm;
import jason.asSyntax.ListTermImpl;
import jason.asSyntax.Literal;
import jason.runtime.Settings;

//import jason.infra.local.RunLocalMAS;

import jason.*;
import jason.runtime.*;
import jason.asSemantics.*;
import jason.asSyntax.*;

import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.*;
import java.util.List;

// FUNCIONAVA SÓ LENDO, AGORA QUERO ESCREVER
// import java.nio.charset.StandardCharsets;

import java.nio.charset.StandardCharsets;
import java.nio.file.StandardOpenOption;


// SÓ PRO RANDOM NO NOME, SE NÃO USAR, TIRAR
import java.util.Random;

//import java.io.File;








// PRO DB
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import java.util.ArrayList;

import java.util.*;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Map;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;



import java.util.stream.Stream;

public class teste extends DefaultInternalAction {

    @Override
    public Object execute(TransitionSystem ts, Unifier un, Term[] args) throws Exception {
        RuntimeServices rs = RuntimeServicesFactory.get();

        Settings s = new Settings();

        // String bels = "agent_id("+12+")";
        String bels = "";

        s.addOption(Settings.INIT_BELS, bels);
        s.addOption(Settings.INIT_GOALS, "a");
        // s.addOption(Settings.INIT_GOALS, "jcm::focus_env_art([art_env('mining','m2view','default')],5)");
        // s.addOption(Settings.INIT_GOALS, "jcm::focus_env_art([art_env('mining','m2view',"+Literal.DefaultNS+")],5)");

        //Aspas Simples
        //s.addOption(Settings.INIT_GOALS, "jcm::focus_env_art([art_env('mining','m2view','default')],5)");
        //Aspas Duplas
        //String aaa = "jcm::focus_env_art([art_env(\"mining\",\"m2view\",\"default\")],5)";
        //System.out.println(aaa);
        //s.addOption(Settings.INIT_GOALS, aaa);
        // s.addOption(Settings.INIT_GOALS, "jcm::focus_env_art([art_env(\"mining\",\"m2view\",\"default\")],5)");

        // Sem Nada
        s.addOption(Settings.INIT_GOALS, "jcm::focus_env_art([art_env(mining,m2view,default)],5)");


        //s.addOption(Settings.INIT_GOALS, "jcm::focus_env_art([art_env(\"mining\",\"m2view\",\""+Literal.DefaultNS+"\")],5)");
        


        //s.addOption(Settings.INIT_GOALS, "jcm::focus_env_art([art_env('mining','m1view')],5)");
        //s.addOption(Settings.INIT_GOALS, "mining");

        rs.createAgent("AAAAAAAAAAAAAAAAA", "miner1.asl", null, null, null, s, ts.getAg());
        rs.startAgent("AAAAAAAAAAAAAAAAA");

        //TimeUnit.SECONDS.sleep(10);

        // JaCaMoAgentParameters ap = null;

        // try {
        //     ap = (JaCaMoAgentParameters)ts.getSettings().getUserParameters().get(Settings.PROJECT_PARAMETER);
        // } catch (Exception e) {
        //     ts.getLogger().warning("error getting parameters to init JaCaMoAgArch! "+e);
        //     return false;
        // }


        // System.out.println("BBB"+ap.getAgName());


        // ListTerm lart = new ListTermImpl();  // list used to produce a goal to join/focus on artifacts
        // ListTerm tail = lart;

        // System.out.println("Início:");
        // System.out.println("getFocus: "+ap.getFocus());
        // Literal art = ASSyntax.createLiteral("art_env",
        //             ASSyntax.createAtom("mining"),  // workspace
        //             ASSyntax.createAtom("m2view"), // art
        //             //ASSyntax.parseTerm("default")); // namespace
        //             Literal.DefaultNS);

        // for (String[] f: ap.getFocus()) {
        //     System.out.println("**********");
        //     System.out.println(f);
        //     Literal art = ASSyntax.createLiteral("art_env",
        //             // ASSyntax.createAtom(f[1]),  // workspace
        //             // ASSyntax.createAtom(f[0]), // art
        //             // ASSyntax.parseTerm(f[2])); // namespace
        //         ASSyntax.createAtom("mining"),  // workspace
        //         ASSyntax.createAtom("m1view"), // art
        //         ASSyntax.parseTerm("default"); // namespace
        //     if (!lart.contains(art))
        //         tail = tail.append(art);
        // }
        System.out.println("Fim");



        // JaCaMoProject jacamo_project = new JaCaMoProject();

        // System.out.println(jacamo_project.toString());

        // JaCaMoRuntimeServices sei_la = JaCaMoRuntimeServices.createAgent;
        // //System.out.println(jacamo_project.getJaCaMoProject().toString());

        // //System.out.println(Arrays.toString(jacamo_project.getWorkspaces()));
        // jacamo_project.addAgFocus("AAAAAAAAAAAAAAAAA",null,"mining.m2view",null);

        // JaCaMoProject jacamo_project = new JaCaMoProject();

        // System.out.println(jacamo_project.toString());
        // //System.out.println(jacamo_project.getJaCaMoProject().toString());

        // //System.out.println(Arrays.toString(jacamo_project.getWorkspaces()));
        // jacamo_project.addAgFocus("AAAAAAAAAAAAAAAAA",null,"mining.m2view",null);

        // JaCaMoProject jacamo_project = new JaCaMoProject();

        // System.out.println(jacamo_project.toString());
        // //System.out.println(jacamo_project.getJaCaMoProject().toString());

        // //System.out.println(Arrays.toString(jacamo_project.getWorkspaces()));
        // jacamo_project.addAgFocus("AAAAAAAAAAAAAAAAA",null,"mining.m2view",null);


        // JaCaMoProject jacamo_project = new JaCaMoProject(RunLocalMAS.getRunner());

        // System.out.println(jacamo_project.toString());
        // //System.out.println(jacamo_project.getJaCaMoProject().toString());

        // //System.out.println(Arrays.toString(jacamo_project.getWorkspaces()));
        // jacamo_project.addAgFocus("AAAAAAAAAAAAAAAAA",null,"mining.m2view",null);

        // // JaCaMoProject jacamo_project = new JaCaMoProject();

        // // System.out.println(jacamo_project.toString());
        // // //System.out.println(jacamo_project.getJaCaMoProject().toString());

        // // //System.out.println(Arrays.toString(jacamo_project.getWorkspaces()));
        // // jacamo_project.addAgFocus("AAAAAAAAAAAAAAAAA",null,"mining.m2view",null);






        // // JaCaMoProject jacamo_project = JaCaMoProject.getJaCaMoProject();

        // // System.out.println(jacamo_project.toString());
        // // //System.out.println(jacamo_project.getJaCaMoProject().toString());

        // // //System.out.println(Arrays.toString(jacamo_project.getWorkspaces()));
        // // jacamo_project.addAgFocus("AAAAAAAAAAAAAAAAA",null,"mining.m2view",null);

        // // // JaCaMoProject jacamo_project = new JaCaMoProject();

        // // // System.out.println(jacamo_project.toString());
        // // // //System.out.println(jacamo_project.getJaCaMoProject().toString());

        // // // //System.out.println(Arrays.toString(jacamo_project.getWorkspaces()));
        // // // jacamo_project.addAgFocus("AAAAAAAAAAAAAAAAA",null,"mining.m2view",null);

        return true;
    }
}