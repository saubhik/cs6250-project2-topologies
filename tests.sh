#!/bin/bash
mkdir -p output

start="$(date +%s%N)"
for filename in *Topo.py; do
  name=$(basename $filename .py)
  python run_spanning_tree.py $name output/$name.txt
done
end="$(date +%s%N)"

passedCounter=0
testCounter=0
for filename in output/*.txt; do
  testCounter=$((testCounter+1))
  name=$(basename $filename .txt)
  if ! diff -q -s output/$name.txt solution/$name.txt > /dev/null; then
    echo "❌ $name failed!"
  else
    echo "✔️ $name passed!"
    passedCounter=$((passedCounter+1))
  fi
done

echo "-----------------------------------------"

if [ "$passedCounter" = "$testCounter" ] ; then
  echo "️✔️ All tests ($passedCounter/$testCounter) passed!"
  elapsed="$((($end-$start)/1000000))"
  echo "Total time taken: $elapsed milliseconds."
else
  echo "❗ Some test(s) failed! ($passedCounter/$testCounter) passed."
fi

echo "-----------------------------------------"
