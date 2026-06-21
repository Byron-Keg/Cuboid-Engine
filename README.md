# 🧊 Cuboid‑Engine
A brute‑force mathematical search engine built to hunt for Perfect Cuboids — one of the oldest unsolved problems in number theory.

---

### ▶️ Run It
Run the search engine:

```
python cuboid_engine.py
```

You can change the search limit on **line 404** of `cuboid_engine.py`  
(advanced users: see lines **398-439** for full range configuration).

---

### 📈 Graphs
After running `cuboid_engine.py`, the output will be saved to **log.txt**.

To generate graphs of your Cuboid Engine data:

```
python Graph.py
```

This will produce a full analysis dashboard of your run.

---

### 🧪 Examples (Grid View)

<table>
  <tr>
    <td align="center">
      <img src="README.md%20Assets/1000%20a.png" width="400"><br>
      <sub>(1000 a — Ryzen 7 7730U)</sub>
    </td>
    <td align="center">
      <img src="README.md%20Assets/5000%20a.png" width="400"><br>
      <sub>(5000 a — Ryzen 7 7730U)</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="README.md%20Assets/10000%20a.png" width="400"><br>
      <sub>(10000 a — Ryzen 7 7730U)</sub>
  </tr>
</table>

---

### 📦 What This Project Does
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

### 📝 License
This project is licensed under the **GPL‑3.0** license.

That means:

- You can use the code  
- You must credit the original author  
- You must release modifications under the same license  
- You cannot make a closed‑source fork  

---

### 🙌 Credits
Created by **Byron Kegley (Byron‑Keg)**


<sup><sub>(Don't mind the sevral commits, I dont use Github that often)</sub></sup>
