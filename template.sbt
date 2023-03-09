Submit-block ::= {
  contact {
    contact {
      name name {
        last "Lera Ramirez",
        first "Manuel",
        middle "",
        initials "",
        suffix "",
        title ""
      },
      affil std {
        affil "University College London",
        div "Genetics, Evolution and Environment",
        city "London",
        country "United Kingdom",
        street "Darwin - GEE, Gower Street",
        email "manuel.lera-ramirez@ucl.ac.uk",
        postal-code "WC1E 6BT"
      }
    }
  },
  cit {
    authors {
      names std {
        {
          name name {
            last "sequenceauthorlastname",
            first "sequenceauthorname",
            middle "",
            initials "M.",
            suffix "",
            title ""
          }
        },
        {
          name name {
            last "sequencelastauthorname",
            first "sequenceauthorname",
            middle "",
            initials "",
            suffix "",
            title ""
          }
        }
      },
      affil std {
        affil "University College London",
        div "Genetics, Evolution and Environment",
        city "London",
        country "United Kingdom",
        street "Darwin - GEE, Gower Street",
        postal-code "WC1E 6BT"
      }
    }
  },
  subtype new
}
Seqdesc ::= pub {
  pub {
    pmid 11859360
  }
}
Seqdesc ::= user {
  type str "DBLink",
  data {
    {
      label str "BioProject",
      num 1,
      data strs {
        "PRJNA13836"
      }
    },
    {
      label str "BioSample",
      num 1,
      data strs {
        "SAMEA3138176"
      }
    }
  }
}
Seqdesc ::= user {
  type str "Submission",
  data {
    {
      label str "AdditionalComment",
      data str "ALT EMAIL:manuel.lera-ramirez@ucl.ac.uk"
    }
  }
}
Seqdesc ::= user {
  type str "Submission",
  data {
    {
      label str "AdditionalComment",
      data str "Submission Title:None"
    }
  }
}
