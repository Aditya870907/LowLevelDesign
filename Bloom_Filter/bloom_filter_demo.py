from core.builder import Builder
from hashing.factory import HashStrategyFactory
from enums.hash_type import HashType
import sys
import uuid

class BloomFilterDemo:
    @staticmethod
    def main():
        # --- 1. Manually Define Parameters ---
        bit_set_size = 10000
        num_hash_functions = 2
        expected_insertions = 1000

        # --- 2. Create a list of Hash Strategies at runtime ---
        strategies = [
            HashStrategyFactory.create(HashType.FNV1A),
            HashStrategyFactory.create(HashType.DJB2),
        ]
        # --- 3. Build the Bloom Filter using the Builder pattern ---
        bloom_filter = (
            Builder()
            .with_bit_set_size(bit_set_size)
            .with_num_hash_functions(num_hash_functions)
            .with_hash_strategies(strategies)
            .build()
        )
        # --- 4. Insert Items into the Bloom Filter ---
        print("\n--- Adding elements to filter ---")
        inserted_elements = []
        for i in range(expected_insertions):
            element = f"user{i}@example.com"
            inserted_elements.append(element)
            bloom_filter.add(element)
        print(f"\n--- {expected_insertions} elements added to filter ---")

        # --- 5. Test Membership (no false negatives) ---
        print("\n--- Verifying no false negatives ---")
        has_false_negatives = False
        for element in inserted_elements:
            if not bloom_filter.might_contain(element):
                print(f"False Negative detected for: {element}", file=sys.stderr)
                has_false_negatives = True
                break
        if not has_false_negatives:
            print("No false negatives detected. Bloom Filter is working correctly.")
        
        # --- 6. test for false positives ---
        print("\n--- Verifying for false positives ---")
        test_set_size = 10000
        false_positive_count = 0
        for i in range(test_set_size):
            random_element = str(uuid.uuid4())
            if bloom_filter.might_contain(random_element):
                false_positive_count += 1
        false_positive_rate = false_positive_count / test_set_size
        print(f"\n--- False Positive Rate: {false_positive_rate:.2%} ---")

if __name__ == "__main__":
    BloomFilterDemo.main()