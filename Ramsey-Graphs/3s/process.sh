for i in x*
do
    echo "Generating pdf for $i ..."
    cat $i | python3 ../print/print.py | dot -Tpdf -o $i".pdf"
    #echo $i".pdf"
done
