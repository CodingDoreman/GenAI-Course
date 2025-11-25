import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";

export const Calculator = () => {
  const [display, setDisplay] = useState("0");
  const [previousValue, setPreviousValue] = useState<number | null>(null);
  const [operation, setOperation] = useState<string | null>(null);
  const [shouldResetDisplay, setShouldResetDisplay] = useState(false);

  const handleNumber = (num: string) => {
    if (shouldResetDisplay) {
      setDisplay(num);
      setShouldResetDisplay(false);
    } else {
      setDisplay(display === "0" ? num : display + num);
    }
  };

  const handleDecimal = () => {
    if (shouldResetDisplay) {
      setDisplay("0.");
      setShouldResetDisplay(false);
    } else if (!display.includes(".")) {
      setDisplay(display + ".");
    }
  };

  const handleOperation = (op: string) => {
    const currentValue = parseFloat(display);
    
    if (previousValue === null) {
      setPreviousValue(currentValue);
    } else if (operation) {
      const result = calculate(previousValue, currentValue, operation);
      setDisplay(String(result));
      setPreviousValue(result);
    }
    
    setOperation(op);
    setShouldResetDisplay(true);
  };

  const calculate = (prev: number, current: number, op: string): number => {
    switch (op) {
      case "+":
        return prev + current;
      case "-":
        return prev - current;
      case "×":
        return prev * current;
      case "÷":
        return prev / current;
      default:
        return current;
    }
  };

  const handleEquals = () => {
    if (operation && previousValue !== null) {
      const result = calculate(previousValue, parseFloat(display), operation);
      setDisplay(String(result));
      setPreviousValue(null);
      setOperation(null);
      setShouldResetDisplay(true);
    }
  };

  const handleClear = () => {
    setDisplay("0");
    setPreviousValue(null);
    setOperation(null);
    setShouldResetDisplay(false);
  };

  const handleBackspace = () => {
    if (display.length === 1) {
      setDisplay("0");
    } else {
      setDisplay(display.slice(0, -1));
    }
  };

  const buttonClass = "h-16 text-lg font-semibold transition-all duration-200 hover:scale-105 active:scale-95";

  return (
    <Card className="w-full max-w-sm p-6 shadow-2xl backdrop-blur-sm bg-card/95">
      <div className="space-y-4">
        {/* Display */}
        <div className="bg-calc-display rounded-2xl p-6 text-right">
          <div className="text-4xl font-bold text-calc-display-text break-all">
            {display}
          </div>
          {operation && (
            <div className="text-sm text-muted-foreground mt-2">
              {previousValue} {operation}
            </div>
          )}
        </div>

        {/* Buttons Grid */}
        <div className="grid grid-cols-4 gap-3">
          {/* Row 1 */}
          <Button
            variant="outline"
            onClick={handleClear}
            className={`${buttonClass} bg-calc-operator hover:bg-calc-operator-hover border-0 col-span-2`}
          >
            C
          </Button>
          <Button
            variant="outline"
            onClick={handleBackspace}
            className={`${buttonClass} bg-calc-operator hover:bg-calc-operator-hover border-0`}
          >
            ⌫
          </Button>
          <Button
            variant="outline"
            onClick={() => handleOperation("÷")}
            className={`${buttonClass} bg-calc-operator hover:bg-calc-operator-hover border-0`}
          >
            ÷
          </Button>

          {/* Row 2 */}
          {["7", "8", "9"].map((num) => (
            <Button
              key={num}
              variant="outline"
              onClick={() => handleNumber(num)}
              className={`${buttonClass} bg-calc-number hover:bg-calc-number-hover border-0`}
            >
              {num}
            </Button>
          ))}
          <Button
            variant="outline"
            onClick={() => handleOperation("×")}
            className={`${buttonClass} bg-calc-operator hover:bg-calc-operator-hover border-0`}
          >
            ×
          </Button>

          {/* Row 3 */}
          {["4", "5", "6"].map((num) => (
            <Button
              key={num}
              variant="outline"
              onClick={() => handleNumber(num)}
              className={`${buttonClass} bg-calc-number hover:bg-calc-number-hover border-0`}
            >
              {num}
            </Button>
          ))}
          <Button
            variant="outline"
            onClick={() => handleOperation("-")}
            className={`${buttonClass} bg-calc-operator hover:bg-calc-operator-hover border-0`}
          >
            -
          </Button>

          {/* Row 4 */}
          {["1", "2", "3"].map((num) => (
            <Button
              key={num}
              variant="outline"
              onClick={() => handleNumber(num)}
              className={`${buttonClass} bg-calc-number hover:bg-calc-number-hover border-0`}
            >
              {num}
            </Button>
          ))}
          <Button
            variant="outline"
            onClick={() => handleOperation("+")}
            className={`${buttonClass} bg-calc-operator hover:bg-calc-operator-hover border-0`}
          >
            +
          </Button>

          {/* Row 5 */}
          <Button
            variant="outline"
            onClick={() => handleNumber("0")}
            className={`${buttonClass} bg-calc-number hover:bg-calc-number-hover border-0 col-span-2`}
          >
            0
          </Button>
          <Button
            variant="outline"
            onClick={handleDecimal}
            className={`${buttonClass} bg-calc-number hover:bg-calc-number-hover border-0`}
          >
            .
          </Button>
          <Button
            onClick={handleEquals}
            className={`${buttonClass} bg-calc-equals hover:bg-calc-equals-hover text-white border-0`}
          >
            =
          </Button>
        </div>
      </div>
    </Card>
  );
};
