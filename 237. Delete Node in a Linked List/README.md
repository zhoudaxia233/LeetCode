# 解题思路：
>[题目链接](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)

我们只能访问到要被删除的节点，而我们可以通过某节点访问到该节点的值和该节点的下一个节点的指针，所以一个很自然的思路就是：**删除给定节点的下一个节点，然后把该给定节点“变成”被删掉的那个节点**。  
具体步骤如下：  
1. 先把下一个节点的值存起来
2. 删掉下一个节点
3. 把之前存起来的值赋给当前节点

---
>注意这道题的特殊性：我们要删除的节点并不是尾节点，因此我们在访问节点的属性的时候不需要担心边界问题，即不必担心当前节点是`None`。  

关于Python的解法：  
`node.val, node.next = node.next.val, node.next.next`  
代码很简单，但此处我们需要理解Python是如何处理以上赋值表达式的。  
处理方法就是：Python把等号右边当成临时变量，先分别按照由左至右的顺序求出它们的值；然后，再分别把临时变量里的值按照由左至右的顺序赋给左边。  
具体说来，就是先求等号右边的`node.next.val`的值(假设结果是`p`)，再求`node.next.next`的值(假设结果是`q`)；然后先把`p`赋给等号左边的`node.val`，再把`q`赋给等号左边的`node.next`。  
你问我怎么知道的？此处强行安利一个库，用法如下：  
```
import dis
dis.dis('node.val, node.next = node.next.val, node.next.next')
```
看不懂没关系，这里有一个关于上述output的解读：  
[请看Delgan的回答](https://stackoverflow.com/questions/12673074/how-should-i-understand-the-output-of-dis-dis)

---
关于C++的解法：
我们可以仿照Python的思路，写一样的代码(但要分成两行来写)，但C++又有自己的特性，C++可以delete，释放内存空间，所以我们就有了如此写法。