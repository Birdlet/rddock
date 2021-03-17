from rdkit import Chem
from rdkit.Chem import AllChem


class Receptor:
    def __init__(self, pdb):
        self.rdmol = self.load_receptor(pdb)
        self._precalculated = None

    def load_receptor(self, pdb):
        recepor = Chem.MolFromPDBFile(pdb)
        return recepor

    def coords(self):
        return self.rdmol.GetConformer(0).GetPositions()

    def set_coords(self, coords):
        if coords.shape[0] != self.rdmol.GetNumAtoms():
            raise TypeError('Atom length')
        for i in range(coords.shape[0]):
            self.rdmol.SetAtomPosition(i, coords[i, :])

    def precalculated(self):
        if not self._precalculated is None:
            return self._precalculated
        pass

            
       

    