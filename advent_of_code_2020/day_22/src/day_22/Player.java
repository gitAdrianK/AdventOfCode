package day_22;

import java.util.ArrayDeque;

public class Player {
	public String name;
	private ArrayDeque<Integer> cards;

	public Player(String name) {
		this.name = name;
		cards = new ArrayDeque<Integer>();
	}

	public void add(int card) {
		this.cards.add(card);
	}

	public int remove() {
		return this.cards.remove();
	}

	public int size() {
		return this.cards.size();
	}

	public boolean isEmpty() {
		return this.cards.isEmpty();
	}

	public ArrayDeque<Integer> getCards() {
		return this.cards;
	}

	public boolean equals(Player other) {
		return this.name.equals(other.name);
	}

	public Player subdeckPlayer(int from, int to) {
		if (from < 0) {
			from = 0;
		}
		if (to > this.cards.size()) {
			to = this.cards.size();
		}
		Player newPlayer = new Player(this.name);
		ArrayDeque<Integer> subQueue = this.cards.clone();
		for (int i = 0; i < from; i++) {
			subQueue.remove();
		}
		for (int i = from; i < to; i++) {
			newPlayer.add(subQueue.remove());
		}
		return newPlayer;
	}

	public Player subdeckPlayer(int to) {
		return this.subdeckPlayer(0, to);
	}

	public Player subdeckPlayer() {
		return this.subdeckPlayer(0, this.cards.size());
	}

	@Override
	public String toString() {
		return this.name + ": " + this.cards.toString();
	}
}
