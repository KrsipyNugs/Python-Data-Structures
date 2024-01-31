def freq_counter(coll):
    counts = {}
    for x in coll:
        counts[x] = counts.get(x, 0) + 1
    return counts

def same_frequency(num1, num2):
    return freq_counter(str(num1)) == freq_counter(str(num2))


same_frequency(551122, 221515)
same_frequency(321142, 3212215)
same_frequency(1212, 2211)