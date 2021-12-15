import kotlin.io.*
import kotlin.collections.List

fun main() {
	val ls = generateSequence(::readLine).map { it.toIntOrNull()!! }.toList()
	val pairs = ls.zip(ls.drop(1))
	println(pairs.filter { it.first < it.second }.toList().size)

	println(ls.zipWithNext { a, b -> a < b }.filter { it }.size)
	println(ls.windowed(3).map { l -> l.sumBy { it } } .zipWithNext { a, b -> a < b}.filter { it }.size)
}
