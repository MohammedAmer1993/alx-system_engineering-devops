#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)\+?[0-9]{11}/).join 
puts ARGV[0].scan(/(?<=to:)\+?[0-9]{11}/).join 
puts ARGV[0].scan(/(?<=flags:)-?[01]:-?[01]:-?[01]:-?[01]:-?[01]/).join 
