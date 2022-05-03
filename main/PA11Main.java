/*
* AUTHOR: Rosemary Kingsley
* FILE: PA11Main.java
* ASSIGNMENT: Programming Assignment 11 - Traveling Salesperson
* COURSE: CSc 210; Section 1; Spring 2022
* PURPOSE: This program performs different algorithms to solve the traveling 
* salesman problem. It begins by reading in a .mtx file and storing it as a 
* directed graph. It then takes in one of the following commands: [HEURISTIC,
* BACKTRACK, MINE, TIME]. 
* 
* - HEURISTIC solves the traveling salesman problem using a heuristic approach. 
* - BACKTRACK uses a recursive backtracking approach.
* - MINE uses an improved recursive backtracking approach that I developed (see 
* README file for more information). 
* 
* Each of the above commands prints the resulting cost and visitOrder for each 
* approach. The TIME command prints the cost and the amount of time it takes to 
* run each of these approaches. 
*
* USAGE: 
* java PA11Main PathTo/infile.mtx [HEURISTIC, BACKTRACK, MINE, TIME]
*
* where infile is the name of a .mtx file in the following format
*
* --------------- EXAMPLE INPUT -----------------
* example.mtx:
* -----------------------------------------------
* | %%MatrixMarket matrix coordinate real general
* | 3 3 6
* | 1 2 1.0
* | 2 1 2.0
* | 1 3 3.0
* | 3 1 4.0
* | 2 3 5.0
* | 3 2 6.0
* -----------------------------------------------
* 
*/

import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;
import java.util.Scanner;

public class PA11Main {

    public static void main(String[] args) throws FileNotFoundException {
        // create directed graph from input .mtx file
        DGraph graph = createGraph(args[0]);

        // solve traveling salesman problem using each approach
        Trip heuristicTrip = handleHeuristic(graph);
        Trip myTrip = handleMine(graph);
        Trip backtrackTrip = handleBacktrack(graph);

        // handle the input command
        if (args[1].equals("HEURISTIC")) {
            System.out.println(heuristicTrip.toString(graph));
        } else if (args[1].equals("MINE")) {
            System.out.println(myTrip.toString(graph));
        } else if (args[1].equals("BACKTRACK")) {
            System.out.println(backtrackTrip.toString(graph));
        } else if (args[1].equals("TIME")) {
            handleTime(graph);
        }
    }

    /*
     * This function reads in a .mtx file and stores it as a directed graph.
     * 
     * @param filename is the name of the .mtx file to be read
     * 
     * @return the directed graph corresponding to the given file
     */
    static DGraph createGraph(String filename) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(filename));
        String currLine = scanner.nextLine();
        while (currLine.charAt(0) == '%') {
            currLine = scanner.nextLine();
        }
        int numNodes = Integer.valueOf(currLine.split("\\s+")[0]);
        int numEdges = Integer.valueOf(currLine.split("\\s+")[2]);

        DGraph graph = new DGraph(numNodes);

        for (int i = 0; i < numEdges; i++) {
            currLine = scanner.nextLine();
            int v = Integer.valueOf(currLine.split("\\s+")[0]);
            int w = Integer.valueOf(currLine.split("\\s+")[1]);
            Double distance = Double.valueOf(currLine.split("\\s+")[2]);
            graph.addEdge(v, w, distance);
        }
        scanner.close();
        return graph;
    }

    /*
     * This function solves the traveling salesman problem using a
     * heuristic approach.
     * 
     * @param graph is the directed graph representing the cities
     * and distances between them
     * 
     * @return the complete trip with cities ordered according to
     * the heuristic approach
     */
    static Trip handleHeuristic(DGraph graph) {
        // create a trip
        Trip myTrip = new Trip(graph.getNumNodes());
        // choose city 1 first, call it the current city
        int currCity = 1;
        myTrip.chooseNextCity(currCity);
        // for each city:
        for (int k = 1; k < graph.getNumNodes(); k++) {
            // find all neighbors of the current city
            List<Integer> neighbors = graph.getNeighbors(currCity);
            // remove neighbors that are not available
            neighbors.removeIf(city -> (!myTrip.isCityAvailable(city)));
            // find the available neighbor that is closest to the current city
            int closestCity = neighbors.get(0);
            double distance = graph.getWeight(currCity, neighbors.get(0));
            for (int i = 1; i < neighbors.size(); i++) {
                if (graph.getWeight(currCity, neighbors.get(i)) < distance) {
                    closestCity = neighbors.get(i);
                    distance = graph.getWeight(currCity, neighbors.get(i));
                }
            }
            // choose the closest city that is available for the trip
            myTrip.chooseNextCity(closestCity);
            // call that closest city the current city
            currCity = closestCity;
        }
        // return the completed trip
        return myTrip;
    }

    /*
     * This function solves the traveling salesman problem using a
     * recursive backtracking approach.
     * 
     * @param graph is the directed graph representing the cities
     * and distances between them
     * 
     * @return the complete trip with cities ordered according to
     * the recursive backtracking approach
     */
    static Trip handleBacktrack(DGraph graph) {
        // create a trip
        Trip tripSoFar = new Trip(graph.getNumNodes());
        // choose city 1 first
        tripSoFar.chooseNextCity(1);
        // call backtrackingFunction on trip and return the minCostTrip found
        return backtrackingFunction(graph, tripSoFar, handleHeuristic(graph));
    }

    /*
     * This is a helper function for the handleBacktrack method.
     * 
     * @param graph is the directed graph representing the cities
     * and distances between them
     * 
     * @param tripSoFar is the partial trip currently being explored
     * 
     * @param minCostTrip is the minimum cost trip found thus far
     * 
     * @return the complete trip with cities ordered according to
     * the recursive backtracking approach
     */
    static Trip backtrackingFunction(DGraph graph, Trip tripSoFar,
            Trip minCostTrip) {
        // if all nodes are in trip:
        if (tripSoFar.isPossible(graph)) {
            // does it have less cost than min trip?
            if (tripSoFar.tripCost(graph) < minCostTrip.tripCost(graph)) {
                // modify min trip previously found
                minCostTrip.copyOtherIntoSelf(tripSoFar);
            }
        }
        // if trip so far has less cost than the min trip previously found
        else if (tripSoFar.tripCost(graph) < minCostTrip.tripCost(graph)) {
            List<Integer> citiesLeft = tripSoFar.citiesLeft();
            // for each city x of the cities left:
            for (int i = 0; i < citiesLeft.size(); i++) {
                // choose x next
                tripSoFar.chooseNextCity(citiesLeft.get(i));
                // explore
                backtrackingFunction(graph, tripSoFar, minCostTrip);
                // unchoose x
                tripSoFar.unchooseLastCity();
            }
        }
        // return the minimum cost trip
        return minCostTrip;
    }

    /*
     * This function solves the traveling salesman problem using my
     * own approach, which is an improved version of recursive
     * backtracking (see README file for more information).
     * 
     * @param graph is the directed graph representing the cities
     * and distances between them.
     * 
     * @return the complete trip with cities ordered according to
     * my improved recursive backtracking approach.
     */
    static Trip handleMine(DGraph graph) {
        // create a trip
        Trip tripSoFar = new Trip(graph.getNumNodes());
        // choose city 1 first
        tripSoFar.chooseNextCity(1);
        // call myBacktrackingFunction on trip and return the minCostTrip found
        return myBacktrackingFunction(graph, tripSoFar, 1,
                handleHeuristic(graph));
    }

    /*
     * This is a helper function for the handleMine method.
     * 
     * @param graph is the directed graph representing the cities
     * and distances between them
     * 
     * @param tripSoFar is the partial trip currently being explored
     * 
     * @param currCity is the last city to be added to tripSoFar
     * 
     * @param minCostTrip is the minimum cost trip found thus far
     * 
     * @return the complete trip with cities ordered according to
     * my improved recursive backtracking approach
     */
    static Trip myBacktrackingFunction(DGraph graph, Trip tripSoFar,
            int currCity, Trip minCostTrip) {
        // if all nodes are in trip:
        if (tripSoFar.isPossible(graph)) {
            // does it have less cost than min trip?
            if (tripSoFar.tripCost(graph) < minCostTrip.tripCost(graph)) {
                // modify min trip previously found
                minCostTrip.copyOtherIntoSelf(tripSoFar);
            }
            return minCostTrip;
        }
        List<Integer> citiesLeft = tripSoFar.citiesLeft();
        // for each city x of the cities left:
        for (int i = 0; i < citiesLeft.size(); i++) {
            // call x the next city
            int nextCity = citiesLeft.get(i);
            // if trip so far plus the distance between the current city and the
            // next city has less cost than the min trip previously found:
            if ((tripSoFar.tripCost(graph) + graph.getWeight(
                    currCity, nextCity)) < minCostTrip.tripCost(graph)) {
                // choose x
                tripSoFar.chooseNextCity(nextCity);
                // explore
                myBacktrackingFunction(graph, tripSoFar, nextCity, minCostTrip);
                // unchoose x
                tripSoFar.unchooseLastCity();
            }
        }
        // return the minimum cost trip
        return minCostTrip;
    }

    /*
     * This function prints the cost and the amount of time it takes to
     * run each approach for solving the traveling salesman problem.
     * 
     * @param graph is the directed graph representing the cities
     * and distances between them.
     */
    static void handleTime(DGraph graph) {
        // find how long it takes the heuristic approach to run
        long startTime = System.nanoTime();
        Trip heuristicTrip = handleHeuristic(graph);
        long endTime = System.nanoTime();
        long duration = (endTime - startTime) / 1000000;
        System.out.println("heuristic: cost = " + heuristicTrip.tripCost(graph)
                + ", " + duration + " milliseconds");

        // find how long it takes my improved backtracking approach to run
        startTime = System.nanoTime();
        Trip myTrip = handleMine(graph);
        endTime = System.nanoTime();
        duration = (endTime - startTime) / 1000000;
        System.out.println("mine: cost = " + myTrip.tripCost(graph) + ", "
                + duration + " milliseconds");

        // find how long it takes the original backtracking approach to run
        startTime = System.nanoTime();
        Trip backtrackTrip = handleBacktrack(graph);
        endTime = System.nanoTime();
        duration = (endTime - startTime) / 1000000;
        System.out.println("backtrack: cost = " + backtrackTrip.tripCost(graph)
                + ", " + duration + " milliseconds");
    }

}
