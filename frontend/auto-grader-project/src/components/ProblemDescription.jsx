// problem description component
export default function ProblemDescription() {
  return (
    <div className="problem-box">
      <h2>Knight Attack</h2>
      <p>
        A knight and a pawn are on a chess board. Find the minimum number of
        moves for the knight to land on the pawn. If impossible, return None.
      </p>

      <pre>
{`Function signature:
def knight_attack(n, kr, kc, pr, pc):`}
      </pre>
    </div>
  );
}
