import json
from datetime import datetime

class VotingSystem:
    def __init__(self):
        self.candidates = {}
        self.voters = set()
        self.votes = {}

    def add_candidate(self, candidate_id, name, position):
        """Add a candidate to the voting system"""
        if candidate_id in self.candidates:
            print(f"Candidate {candidate_id} already exists!")
            return False

        self.candidates[candidate_id] = {
            'name': name,
            'position': position,
            'votes': 0
        }
        self.votes[candidate_id] = 0
        print(f"✓ {name} added as candidate for {position}")
        return True

    def register_voter(self, voter_id, voter_name):
        """Register a voter"""
        if voter_id in self.voters:
            print(f"Voter {voter_id} is already registered!")
            return False

        self.voters.add(voter_id)
        print(f"✓ {voter_name} registered to vote")
        return True

    def cast_vote(self, voter_id, candidate_id):
        """Cast a vote for a candidate"""
        # Check if voter is registered
        if voter_id not in self.voters:
            print(f"❌ Voter {voter_id} is not registered!")
            return False

        # Check if voter already voted
        if voter_id in [v for v in self.voters if v in self.votes]:
            if self.votes.get(voter_id) is not None:
                print(f"❌ Voter {voter_id} has already voted!")
                return False

        # Check if candidate exists
        if candidate_id not in self.candidates:
            print(f"❌ Candidate {candidate_id} does not exist!")
            return False

        # Record vote
        self.votes[candidate_id] = self.votes.get(candidate_id, 0) + 1
        self.candidates[candidate_id]['votes'] += 1
        print(f"✓ Vote recorded for {self.candidates[candidate_id]['name']}")
        return True

    def display_candidates(self):
        """Display all candidates"""
        if not self.candidates:
            print("No candidates registered yet!")
            return

        print("\n" + "="*50)
        print("CANDIDATES")
        print("="*50)
        for cid, candidate in self.candidates.items():
            print(f"ID: {cid} | Name: {candidate['name']} | Position: {candidate['position']}")
        print("="*50 + "\n")

    def display_results(self):
        """Display voting results"""
        if not self.candidates:
            print("No candidates to display!")
            return

        print("\n" + "="*60)
        print("ELECTION RESULTS")
        print("="*60)

        # Sort by votes
        sorted_candidates = sorted(
            self.candidates.items(),
            key=lambda x: x[1]['votes'],
            reverse=True
        )

        total_votes = sum(c['votes'] for c in self.candidates.values())

        for rank, (cid, candidate) in enumerate(sorted_candidates, 1):
            votes = candidate['votes']
            percentage = (votes / total_votes * 100) if total_votes > 0 else 0
            print(f"{rank}. {candidate['name']} ({candidate['position']})")
            print(f"   Votes: {votes} ({percentage:.1f}%)")
            print()

        print(f"Total Votes Cast: {total_votes}")
        print("="*60 + "\n")

    def get_winner(self):
        """Get the candidate with most votes"""
        if not self.candidates:
            return None

        winner = max(self.candidates.items(), key=lambda x: x[1]['votes'])
        return winner


def main():
    system = VotingSystem()

    print("🗳️  COLLEGE ELECTION VOTING SYSTEM 🗳️\n")

    while True:
        print("\nOPTIONS:")
        print("1. Add Candidate")
        print("2. Register Voter")
        print("3. Cast Vote")
        print("4. View Candidates")
        print("5. View Results")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            candidate_id = input("Enter candidate ID: ").strip()
            name = input("Enter candidate name: ").strip()
            position = input("Enter position (President/Vice President/etc): ").strip()
            system.add_candidate(candidate_id, name, position)

        elif choice == '2':
            voter_id = input("Enter voter ID: ").strip()
            voter_name = input("Enter voter name: ").strip()
            system.register_voter(voter_id, voter_name)

        elif choice == '3':
            voter_id = input("Enter voter ID: ").strip()
            candidate_id = input("Enter candidate ID to vote for: ").strip()
            system.cast_vote(voter_id, candidate_id)

        elif choice == '4':
            system.display_candidates()

        elif choice == '5':
            system.display_results()

        elif choice == '6':
            print("\n✓ Thank you for using the Voting System!")
            break

        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
