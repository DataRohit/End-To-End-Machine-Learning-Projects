def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('a')),
            ('T',seq.count('t')),
            ('G',seq.count('g')),
            ('C',seq.count('c'))
            ])
  return d