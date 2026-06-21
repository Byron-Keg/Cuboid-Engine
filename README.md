# 🧊 Cuboid‑Engine
A brute‑force mathematical search engine built to hunt for Perfect Cuboids — one of the oldest unsolved problems in number theory.

---

## ▶️ Run It
Run the search engine:

```
python cuboid_engine.py
```

You can change the search limit on **line 425** of `cuboid_engine.py`  
(advanced users: see lines **423–471** for full range configuration).

---

## 📈 Graphs
After running `cuboid_engine.py`, the output will be saved to **log.txt**.

To generate graphs of your Cuboid Engine data:

```
python Graph.py
```

This will produce a full analysis dashboard of your run.

---

## 📦 What This Project Does
The Cuboid‑Engine attempts to find integer solutions to the **Perfect Cuboid Problem**, where a rectangular box has:

- all edges as integers  
- all face diagonals as integers  
- the space diagonal as an integer  

Mathematically, it checks:

- a² + b² = d₁²  
- a² + c² = d₂²  
- b² + c² = d₃²  
- a² + b² + c² = D²  

---

## 📝 License
This project is licensed under the **GPL‑3.0** license.

That means:

- You can use the code  
- You must credit the original author  
- You must release modifications under the same license  
- You cannot make a closed‑source fork  

---

## 🙌 Credits
Created by **Byron Kegley (Byron‑Keg)**
