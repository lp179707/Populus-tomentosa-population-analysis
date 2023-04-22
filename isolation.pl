#!/bin/perl #-w

open(IN,"A.txt"); # acquried NO file
open(IN2,"B.txt"); # aim database file

open(OUT,">3_results.txt"); # aim results


my @acc=<IN>;
@b= map {split '\s+', $_} @acc;
@acc=@b;

while(<IN2>){

    foreach $acc(@acc){
	if(/$acc/){
              print OUT $_;
        }
    }
}

