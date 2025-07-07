To verify if a number k corresponds to a checksum d using a generated pattern (called a Ruban).

🔧 How It Works:
Ruban(k, d, t)
Generates a mask array t, where each element is:
10^position mod d — used to "weight" each digit of k.

somme(t, k)
Multiplies each digit of k by the corresponding value in t, then adds the results to get a sum s.

verif(k, d, t)
Repeats the sum + ruban generation until the number of digits in k matches the number of digits in d.
Then checks if the final sum equals d.

✅ Output:
The mask (t)

A tuple: (True/False, final_k) depending on whether the check passes
