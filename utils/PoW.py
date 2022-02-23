import KnowledgeChain as KC

class ProofOfWork:
    def __init__(self):
        self.blockchain = KC.get_blockchain_from_memory()
        self.new_block = None

    def get_contribution_incentive(self, contributions: list) -> int:
        contribution_incentive = 0
        for contribution in contributions:
            input_amount = 0
            output_amount = 0
            for contribution_input in contribution["inputs"]:
                utxo = self.blockchain.get_contribution_from_utxo(contribution_input["contribution_hash"])
                if utxo:
                    utxo_amount = utxo["outputs"][contribution_input["output_index"]]["amount"]
                    input_amount = input_amount + utxo_amount
            for contribution_output in contribution["outputs"]:
                output_amount = output_amount + contribution_output["amount"]
            contribution_incentive = contribution_incentive + (input_amount-output_amount)
        return contribution_incentive