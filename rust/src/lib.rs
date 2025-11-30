pub mod runner {
    use anyhow::{bail, Context, Result};
    use std::fs;

    pub type Solver = fn(&str) -> Result<i64>;

    pub fn run(part1: Solver, part2: Solver) -> Result<()> {
        let mut args = std::env::args().skip(1);
        let part = args
            .next()
            .context("expected a part argument (part1 or part2)")?;
        let path = args
            .next()
            .context("expected an input path argument")?;

        let contents = fs::read_to_string(&path)
            .with_context(|| format!("failed to read input file: {path}"))?;

        let answer = match part.as_str() {
            "part1" => part1(&contents)?,
            "part2" => part2(&contents)?,
            other => bail!("unknown part '{other}'"),
        };

        println!("{answer}");
        Ok(())
    }
}
