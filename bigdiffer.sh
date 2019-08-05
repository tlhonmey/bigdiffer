#! /bin/bash -e

EXEDIR=`dirname $0`

LEFT=`realpath $1`
RIGHT=`realpath $2`

echo "chunking..."
$EXEDIR/chunker $LEFT > left.chunks &
$EXEDIR/chunker $RIGHT > right.chunks &

time wait
echo "hashing..."
python2 $EXEDIR/hasher.py "$LEFT" left.chunks left.hashed & 
python2 $EXEDIR/hasher.py "$RIGHT" right.chunks right.hashed & 

time wait
echo "indexing..."
time python2 $EXEDIR/dbloader.py left.hashed left.db
echo "comparing..."
time python2 $EXEDIR/dbdiffcomp.py left.db right.hashed > diff.dirty
echo "discarding unneded control data..."
time cat diff.dirty | cut -d"|" -f1,2 > $3.control
echo "compacting control file"
time perl controlcompactor.pl $3.control > $3.control.compact
mv $3.control.compact $3.control
echo "compiling data file..."
time python2 $EXEDIR/chunkgrabber.py $RIGHT $3.control $3.data

echo "testing patch:"
echo "  applying..."
time python2 $EXEDIR/patcher.py $LEFT $3.data $3.control $3.patchtest
echo "  verifying..."
time diff $RIGHT $3.patchtest
echo "Cleaning up..."
time rm left.chunks right.chunks left.hashed right.hashed left.db diff.dirty $3.patchtest
echo "DONE."
echo "patch consists of $3.control and $3.data  compress them with tool of your choice."
echo "I recommend xz -9e --lzma2=dict=1G  But adjust to suit your application."
