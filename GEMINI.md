# Documentation Rule for Notebooks

## Auto Docstring Markdown Cells

Jab bhi user kisi `.ipynb` (Jupyter Notebook) file mein kaam kare aur code likhe, toh:

1. **Har code cell ke upar ya beech mein ek markdown cell add karo** jo us code ka documentation/docstring explain kare.
2. Markdown cell mein likho:
   - Function/class ka **naam** aur **purpose** (Hindi + English mix mein, user ke style mein)
   - **Parameters** aur **return values** ka short description
   - Agar koi important logic hai toh uska **brief explanation**
3. Format: Markdown cell mein proper headings (`###`), bullet points, aur code references use karo.
4. Ye markdown cells **notebook ke andar hi** code cells ke beech insert karo — koi alag file mat banao.
5. Docstrings **Hindi-English mix** mein likho (user ki preferred language).
6. Har naye code cell ke liye ek corresponding markdown documentation cell hona chahiye.
