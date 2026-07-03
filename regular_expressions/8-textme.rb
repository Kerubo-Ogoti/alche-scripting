#!/usr/bin/env ruby
input = ARGV[0]

from = input.scan(/\[from:([^\]]+)\]/).flatten.join
to = input.scan(/\[to:([^\]]+)\]/).flatten.join
flags = input.scan(/\[flags:([^\]]+)\]/).flatten.join

puts "#{from},#{to},#{flags}"
