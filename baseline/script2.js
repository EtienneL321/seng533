import { browser } from "k6/experimental/browser";
import { check } from "k6";
import exec from "k6/execution";

export const options = {
  scenarios: {
    ui: {
      executor: "shared-iterations",
      options: {
        browser: {
          type: "chromium",
        },
      },
      vus: 1,
      iterations: 50,
    },
  },
  thresholds: {
    checks: ["rate==1.0"],
  },
};

export default async function () {
  /* Create page element */
  const page = browser.newPage();

  try {
    /* Populate page element */
    await page.goto("https://djaq3qtxdz92e.cloudfront.net/");

    /* Fill id and username for "Create User" field */
    let id = exec.vu.idInInstance;
    page.locator("(//input[@id='userId'])[1]").type(id);
    let username = "user" + id.toString();
    page.locator("//*[@id='userName']").type(username);

    /* Get Buttons */
    let createUserButton = page.locator(
      "//*[@id='app']/div[2]/form/div[3]/button"
    );
    let getUserButton = page.locator(
      "//*[@id='app']/div[3]/form/div[2]/button"
    );

    /* Press "Create User" button and wait 3s */
    await Promise.all([page.waitForTimeout(3000), createUserButton.click()]);

    /* Fill id for "Get User By ID" field */
    page.locator("(//input[@id='userId'])[2]").type(id);

    /* Pres "Get User" button and wait 3s */
    await Promise.all([page.waitForFunction(3000), getUserButton.click()]);

    /* Check that new user was successfully created */
    let ans = id.toString() + " . " + username;
    check(page, {
      userAddedSuccessfully: (p) =>
        p.locator("//*[@id='app']/div[3]/h3").textContent() == ans,
    });
  } finally {
    page.close();
  }
}
