"""
EmotionCipher - Interactive Demo Application
Main entry point for demonstrating the emotion-preserving encryption system.
"""

from emotion_cipher import EmotionCipher
import sys


def print_banner():
    """Print the application banner."""
    print("\n" + "="*70)
    print(" "*20 + "🔐 EMOTION CIPHER 🔐")
    print(" "*10 + "Empathy Encryption - Where Feelings Stay Readable")
    print("="*70 + "\n")


def run_example_demos():
    """Run the three example cases from the problem statement."""
    print("\n" + "🎯 RUNNING PROVIDED EXAMPLES" + "\n")
    
    cipher = EmotionCipher()
    
    # Example 1
    example1 = "Feeling ecstatic about joining the new AI research team, though a bit anxious about the deadlines ahead."
    cipher.demo_example(example1)
    
    # Example 2
    example2 = "I can't believe I failed that test again. I'm so disappointed and frustrated right now."
    cipher.demo_example(example2)
    
    # Example 3
    example3 = "Finally got the job offer! I'm thrilled and can't wait to start this new journey."
    cipher.demo_example(example3)


def interactive_mode():
    """Run the application in interactive mode."""
    cipher = EmotionCipher()
    
    while True:
        print("\n" + "-"*70)
        print("What would you like to do?")
        print("1. Encrypt a message")
        print("2. View example demonstrations")
        print("3. Exit")
        print("-"*70)
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\n" + "="*70)
            message = input("Enter your message to encrypt: ").strip()
            
            if message:
                cipher.demo_example(message)
            else:
                print("❌ Empty message. Please try again.")
        
        elif choice == "2":
            run_example_demos()
        
        elif choice == "3":
            print("\n" + "="*70)
            print("Thank you for using EmotionCipher! 🔐")
            print("="*70 + "\n")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


def main():
    """Main entry point."""
    print_banner()
    
    # Check if command-line arguments provided
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo" or sys.argv[1] == "-d":
            # Run examples
            run_example_demos()
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("Usage:")
            print("  python main.py              - Run in interactive mode")
            print("  python main.py --demo       - Run example demonstrations")
            print("  python main.py --help       - Show this help message")
            print()
        else:
            # Treat as a message to encrypt
            message = " ".join(sys.argv[1:])
            cipher = EmotionCipher()
            cipher.demo_example(message)
    else:
        # Run in interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
