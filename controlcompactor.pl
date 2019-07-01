#! /usr/bin/perl
#

$filename = $ARGV[0];
open(INFILE, "<$filename");



$lastline=<INFILE>;
chomp($lastline);
($llside,$llrange)=split(/\|/,"$lastline");
($lls,$lle)=split (/\-/,$llrange);


while ($thisline = <INFILE>) {
  chomp($thisline);
  ($tlside,$tlrange)=split(/\|/,$thisline);
  ($tls,$tle)=split(/\-/,$tlrange);


  if ( ($tlside eq $llside) && ($tls == $lle) ) {
       $lle=$tle;
  }
  else   {
    print "$llside|$lls-$lle\n";
    $lastline=$thisline;
    $llside=$tlside;
    $lls=$tls;
    $lle=$tle;
  }
    
 
}
print "$llside|$lls-$lle\n";
