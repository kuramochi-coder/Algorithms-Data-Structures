readline() #skip first line
nums = [parse(Int, x) for x in readlines()]
f = x->1.0/x
println(Int(round(60.0/sum(f.(nums)))))
