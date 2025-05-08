import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input: string[] = [];

rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  solve();
});

type Tree = {
  [key: string]: [string, string]; // 노드: [왼쪽 자식, 오른쪽 자식]
};

const tree: Tree = {};

function solve() {
  const N: number = parseInt(input[0]);
  
  // 트리 구성
  for (let i = 1; i <= N; i++) {
    const [parent, left, right] = input[i].split(' ');
    tree[parent] = [left, right];
  }

  const preorder: string[] = [];
  const inorder: string[] = [];
  const postorder: string[] = [];

  function dfs(node: string) {
    if (node === '.') return;

    const [left, right] = tree[node];

    // 전위순회: 현재 → 왼쪽 → 오른쪽
    preorder.push(node);
    dfs(left);
    // 중위순회: 왼쪽 → 현재 → 오른쪽
    inorder.push(node);
    dfs(right);
    // 후위순회: 왼쪽 → 오른쪽 → 현재
    postorder.push(node);
  }

  function preOrder(node: string) {
    if (node === '.') return;
    const [left, right] = tree[node];
    preorder.push(node);
    preOrder(left);
    preOrder(right);
  }

  function inOrder(node: string) {
    if (node === '.') return;
    const [left, right] = tree[node];
    inOrder(left);
    inorder.push(node);
    inOrder(right);
  }

  function postOrder(node: string) {
    if (node === '.') return;
    const [left, right] = tree[node];
    postOrder(left);
    postOrder(right);
    postorder.push(node);
  }

  preOrder('A');
  inOrder('A');
  postOrder('A');

  console.log(preorder.join(''));
  console.log(inorder.join(''));
  console.log(postorder.join(''));
}
