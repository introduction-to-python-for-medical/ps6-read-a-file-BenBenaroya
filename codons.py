def create_codon_dict(file_path):
  file = open(file_path)
  rows = file.readlines()
  file.close()

  mapping_c_a = {}
  for row in rows:
    cell = row.strip().split('\t')
    mapping_c_a[cell[0]] = cell[2]
  return mapping_c_a


